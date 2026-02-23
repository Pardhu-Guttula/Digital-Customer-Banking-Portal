# Epic Title: Implement role-based access control for user authorization

CREATE TABLE role_permissions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    role_id INT NOT NULL,
    permission VARCHAR(255) NOT NULL,
    FOREIGN KEY (role_id) REFERENCES roles(id) ON DELETE CASCADE
);