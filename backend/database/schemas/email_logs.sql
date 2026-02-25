# Epic Title: Log Email Communication in PostgreSQL

CREATE TABLE email_logs (
    id SERIAL PRIMARY KEY,
    request_id INT NOT NULL,
    status VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    sent_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    delivery_status VARCHAR(10) NOT NULL,
    UNIQUE (request_id, status, delivery_status)
);