# Epic Title: Data Storage and Retrieval Using PostgreSQL

CREATE TABLE sales_data (
    id SERIAL PRIMARY KEY,
    product_id INT NOT NULL,
    quantity_sold INT NOT NULL,
    total_revenue FLOAT NOT NULL,
    sale_timestamp TIMESTAMP NOT NULL,
    FOREIGN KEY (product_id) REFERENCES products(id)
);