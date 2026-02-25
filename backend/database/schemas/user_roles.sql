# Epic Title: Enforce Role-Based Access Control Using FastAPI

CREATE TABLE user_roles (
    user_id INT PRIMARY KEY,
    role_id INT,
    FOREIGN KEY (role_id) REFERENCES roles(role_id)
);