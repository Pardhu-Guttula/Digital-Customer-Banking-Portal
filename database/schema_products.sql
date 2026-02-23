# Epic Title: Implement Product Recommendations Based on User Preferences

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    price FLOAT NOT NULL,
    stock INT NOT NULL,
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP
);