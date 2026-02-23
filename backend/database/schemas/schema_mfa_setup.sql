# Epic Title: Multi-Factor Authentication Setup

CREATE TABLE mfa_setup (
    id SERIAL PRIMARY KEY,
    account_id INTEGER NOT NULL,
    mfa_method VARCHAR NOT NULL,
    is_active BOOLEAN DEFAULT FALSE
);