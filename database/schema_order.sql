# Epic Title: Integrate with PostgreSQL for Data Storage

CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    address_id INT NOT NULL,
    total_amount FLOAT NOT NULL,
    status_id INT NOT NULL,
    date TIMESTAMP NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (address_id) REFERENCES addresses(id),
    FOREIGN KEY (status_id) REFERENCES statuses(id)
);