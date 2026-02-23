# Epic Title: Track and Analyze Sales Data

CREATE TABLE sales_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT NOT NULL,
    quantity_sold INT NOT NULL,
    total_revenue FLOAT NOT NULL,
    sale_timestamp TIMESTAMP NOT NULL,
    FOREIGN KEY (product_id) REFERENCES products(id)
);