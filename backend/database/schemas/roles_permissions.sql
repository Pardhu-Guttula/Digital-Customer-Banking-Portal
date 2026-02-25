# Epic Title: Enforce Role-Based Access Control Using FastAPI

CREATE TABLE roles_permissions (
    role_id INT,
    permission_id INT,
    FOREIGN KEY (role_id) REFERENCES roles(role_id),
    FOREIGN KEY (permission_id) REFERENCES permissions(permission_id)
);