# Epic Title: Dynamic and Interactive Dashboard UI using React

import React from 'react';

const ServiceWidget = ({ service, onClick }) => {
    const handleClick = () => {
        onClick(service.id);
    };

    return (
        <div className="widget" onClick={handleClick}>
            <h3>{service.name}</h3>
            <p>{service.description}</p>
        </div>
    );
};

export default ServiceWidget;