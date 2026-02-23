# Epic Title: Track and Analyze User Behavior

CREATE TABLE user_behavior (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    action VARCHAR(255) NOT NULL,
    detail TEXT,
    timestamp TIMESTAMP NOT NULL
);