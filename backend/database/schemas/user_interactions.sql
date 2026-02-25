# Epic Title: Store User Interaction Data in PostgreSQL

CREATE TABLE user_interactions (
    id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    interaction_type VARCHAR(50) NOT NULL,
    interaction_data JSONB,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users (id)
);