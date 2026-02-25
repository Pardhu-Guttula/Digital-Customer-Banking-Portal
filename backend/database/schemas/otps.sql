# Epic Title: Implement User Authentication with Multi-Factor Authentication

CREATE TABLE otps (
    email VARCHAR(255) UNIQUE NOT NULL,
    otp VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);