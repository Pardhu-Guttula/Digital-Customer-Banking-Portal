# Epic Title: Secure Login System with MFA

CREATE TABLE mfa_setup (
    id SERIAL PRIMARY KEY,
    account_id INTEGER NOT NULL,
    mfa_method VARCHAR NOT NULL,
    is_active BOOLEAN DEFAULT TRUE
);