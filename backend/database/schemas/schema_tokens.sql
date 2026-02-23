# Epic Title: Multi-Factor Authentication Setup

CREATE TABLE tokens (
    id SERIAL PRIMARY KEY,
    account_id INTEGER NOT NULL,
    token VARCHAR NOT NULL,
    is_valid BOOLEAN DEFAULT TRUE,
    expires_at TIMESTAMP NOT NULL
);