# Epic Title: Dynamic and Interactive Dashboard UI using React

import React, { useEffect, useState } from 'react';
import axios from 'axios';
import ProductWidget from './ProductWidget';
import ServiceWidget from './ServiceWidget';

const Dashboard = ({ userId }) => {
    const [data, setData] = useState({});
    const [error, setError] = useState('');

    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await axios.get('/api/dashboard', { params: { user_id: userId }});
                setData(response.data);
            } catch (err) {
                setError('Error fetching dashboard data');
            }
        };
        fetchData();
    }, [userId]);

    const handleWidgetClick = (widgetId) => {
        // Handle widget click logic, e.g., open details, refresh data, etc.
        console.log(`Widget clicked: ${widgetId}`);
    }

    if (error) {
        return <p>{error}</p>;
    }

    if (!data.user_profile) {
        return <p>User profile data missing</p>;
    }

    return (
        <div>
            <h1>Welcome, {data.user_profile.name}</h1>
            <div>
                <h2>Banking Products</h2>
                {data.banking_products.map(product => (
                    <ProductWidget key={product.id} product={product} onClick={handleWidgetClick} />
                ))}
            </div>
            <div>
                <h2>Services</h2>
                {data.services.map(service => (
                    <ServiceWidget key={service.id} service={service} onClick={handleWidgetClick} />
                ))}
            </div>
        </div>
    );
};

export default Dashboard;