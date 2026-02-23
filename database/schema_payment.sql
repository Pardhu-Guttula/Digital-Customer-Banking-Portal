# Epic Title: Store Order and Payment Information in PostgreSQL

CREATE TABLE payments (
    id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    order_id INT NOT NULL,
    card_number VARCHAR(19) NOT NULL,
    card_expiry VARCHAR(5) NOT NULL,
    card_cvv VARCHAR(4) NOT NULL,
    amount FLOAT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (order_id) REFERENCES orders(id)
);