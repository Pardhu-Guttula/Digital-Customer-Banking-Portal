# Epic Title: PostgreSQL Integration for Service Modification Requests

CREATE TABLE service_modifications (
    id SERIAL PRIMARY KEY,
    service_name VARCHAR(100) NOT NULL,
    modification_details TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);