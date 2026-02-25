# File: tests/test_user_repository.py

import pytest
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from your_module_name import UserRepository

# Mock database connection string
DATABASE_URL = "sqlite:///:memory:"

# Initialize the test database
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
db_session = Session()

@pytest.fixture
def user_repository():
    return UserRepository(db_session)

@pytest.fixture(autouse=True)
def setup_tables():
    # Create tables... (define the required schema, e.g., users, roles, ...) 
    db_session.execute('''
    CREATE TABLE roles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE
    )''')
    db_session.execute('''
    CREATE TABLE users (
        id TEXT PRIMARY KEY,
        role_id INTEGER,
        FOREIGN KEY(role_id) REFERENCES roles(id)
    )''')
    db_session.execute('''
    CREATE TABLE role_permissions (
        permission TEXT NOT NULL, 
        role_id INTEGER, 
        FOREIGN KEY(role_id) REFERENCES roles(id)
    )''')
    db_session.commit()
    yield
    db_session.execute('DROP TABLE role_permissions')
    db_session.execute('DROP TABLE users')
    db_session.execute('DROP TABLE roles')
    db_session.commit()

@pytest.mark.parametrize("user_id, role", [
    ("user1", "admin"),
    ("user2", "editor"),
])
def test_assign_role(user_repository, user_id, role):
    # Insert roles
    db_session.execute("INSERT INTO roles (name) VALUES ('admin')")
    db_session.execute("INSERT INTO roles (name) VALUES ('editor')")
    db_session.commit()

    # Assign role
    user_repository.assign_role(user_id, role)
    role_id = db_session.execute("SELECT id FROM roles WHERE name = ?", (role,)).fetchone()[0]
    user_role_id = db_session.execute("SELECT role_id FROM users WHERE id = ?", (user_id,)).fetchone()[0]
    assert user_role_id == role_id

@pytest.mark.parametrize("user_id, expected_permissions", [
    ("user1", ["read", "write"]),
    ("user2", ["read"]),
])
def test_get_user_permissions(user_repository, user_id, expected_permissions):
    # Insert roles and permissions
    db_session.execute("INSERT INTO roles (name) VALUES ('admin')")
    db_session.execute("INSERT INTO roles (name) VALUES ('editor')")
    roles = db_session.execute("SELECT id FROM roles").fetchall()
    role_ids = {row['name']: row['id'] for row in roles}

    db_session.execute("INSERT INTO role_permissions (permission, role_id) VALUES ('read', ?)", (role_ids['admin'],))
    db_session.execute("INSERT INTO role_permissions (permission, role_id) VALUES ('write', ?)", (role_ids['admin'],))
    db_session.execute("INSERT INTO role_permissions (permission, role_id) VALUES ('read', ?)", (role_ids['editor'],))
    db_session.commit()

    # Assign roles to users
    db_session.execute("INSERT INTO users (id, role_id) VALUES (?, ?)", ("user1", role_ids['admin']))
    db_session.execute("INSERT INTO users (id, role_id) VALUES (?, ?)", ("user2", role_ids['editor']))
    db_session.commit()

    # Get permissions
    permissions = user_repository.get_user_permissions(user_id)
    assert permissions == expected_permissions


def test_assign_role_invalid_role(user_repository):
    user_id = "user1"
    invalid_role = "nonexistent_role"
    with pytest.raises(Exception):
        user_repository.assign_role(user_id, invalid_role)


def test_get_user_permissions_no_permissions(user_repository):
    user_id = "user1"
    db_session.execute("INSERT INTO users (id, role_id) VALUES (?, NULL)", (user_id,))
    db_session.commit()
    permissions = user_repository.get_user_permissions(user_id)
    assert permissions == []
