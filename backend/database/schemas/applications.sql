# Epic Title: Save Incomplete Applications

CREATE TABLE applications (
    user_id INT PRIMARY KEY,
    application_data JSONB NOT NULL,
    saved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);