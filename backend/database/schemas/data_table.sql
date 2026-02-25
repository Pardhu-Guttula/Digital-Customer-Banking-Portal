# Epic Title: Secure Role-Based Data Segregation in PostgreSQL

CREATE TABLE data_table (
    id SERIAL PRIMARY KEY,
    data BYTEA NOT NULL,
    role VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);