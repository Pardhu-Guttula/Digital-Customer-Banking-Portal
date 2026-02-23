# Epic Title: Document Upload

CREATE TABLE documents (
    id INT AUTO_INCREMENT PRIMARY KEY,
    filename VARCHAR(255) UNIQUE NOT NULL,
    path VARCHAR(255) NOT NULL
);