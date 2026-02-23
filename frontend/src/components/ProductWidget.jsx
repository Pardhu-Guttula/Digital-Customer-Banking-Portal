# Epic Title: Dynamic and Interactive Dashboard UI using React

import React from 'react';

const ProductWidget = ({ product, onClick }) => {
    const handleClick = () => {
        onClick(product.id);
    };

    return (
        <div className="widget" onClick={handleClick}>
            <h3>{product.name}</h3>
            <p>{product.description}</p>
        </div>
    );
};

export default ProductWidget;