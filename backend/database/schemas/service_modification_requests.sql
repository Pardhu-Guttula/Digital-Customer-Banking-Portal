# Epic Title: Develop React UI for Submitting Service Modification Requests

CREATE TABLE service_modification_requests (
    id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    service_type VARCHAR(255) NOT NULL,
    modification_details TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);