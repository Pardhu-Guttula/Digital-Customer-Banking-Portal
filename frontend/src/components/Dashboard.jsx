# Epic Title: Dashboard Backend Data Integration

import React, { useEffect, useState } from 'react';
import axios from 'axios';

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
                    <div key={product.id}>
                        <h3>{product.name}</h3>
                        <p>{product.description}</p>
                    </div>
                ))}
            </div>
            <div>
                <h2>Services</h2>
                {data.services.map(service => (
                    <div key={service.id}>
                        <h3>{service.name}</h3>
                        <p>{service.description}</p>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default Dashboard;