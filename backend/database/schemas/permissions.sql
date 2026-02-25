# Epic Title: Implement Role-Based Access Controls for User Authorization

CREATE TABLE permissions (
    permission_id SERIAL PRIMARY KEY,
    permission_name VARCHAR(255) NOT NULL
);