# Epic Title: Data Storage and Retrieval Using PostgreSQL

CREATE TABLE user_behavior (
    id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    action VARCHAR(255) NOT NULL,
    detail TEXT,
    timestamp TIMESTAMP NOT NULL
);