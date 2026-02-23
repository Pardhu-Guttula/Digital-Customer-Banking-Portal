# Epic Title: Address Entry in Checkout Process

CREATE TABLE addresses (
    id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    street VARCHAR(100) NOT NULL,
    city VARCHAR(50) NOT NULL,
    state VARCHAR(50) NOT NULL,
    postal_code VARCHAR(10) NOT NULL,
    country VARCHAR(50) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);