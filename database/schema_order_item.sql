# Epic Title: Integrate with PostgreSQL for Data Storage

CREATE TABLE order_items (
    id SERIAL PRIMARY KEY,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    price FLOAT NOT NULL,
    order_id INT,
    FOREIGN KEY (order_id) REFERENCES orders(id)
);