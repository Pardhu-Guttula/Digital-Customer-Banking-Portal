# Epic Title: Integrate Self-Service Portal with Core Banking System

CREATE TABLE local_table (
    id SERIAL PRIMARY KEY,
    data JSONB NOT NULL,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);