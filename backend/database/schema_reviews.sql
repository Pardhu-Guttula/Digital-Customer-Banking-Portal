# Epic Title: Enable Users to Leave Reviews and Ratings for Products

CREATE TABLE reviews (
    id SERIAL PRIMARY KEY,
    content VARCHAR(500) NOT NULL,
    rating INT NOT NULL CHECK (rating >= 1 AND rating <= 5),
    product_id INT NOT NULL,
    user_id INT NOT NULL,
    UNIQUE (user_id, product_id),
    FOREIGN KEY (product_id) REFERENCES products(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);