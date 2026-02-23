# Epic Title: Save incomplete application state

CREATE TABLE application_states (
    user_id VARCHAR(255) PRIMARY KEY,
    state TEXT NOT NULL
);