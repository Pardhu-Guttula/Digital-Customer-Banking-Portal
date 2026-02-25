# Epic Title: FastAPI Email Notification Service

CREATE TABLE email_logs (
    id SERIAL PRIMARY KEY,
    request_id INT NOT NULL,
    status VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    sent_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (request_id, status)
);