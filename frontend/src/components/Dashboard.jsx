# Epic Title: Personalized Dashboard Layout

import React, { useEffect, useState } from 'react';
import axios from 'axios';

const Dashboard = ({ userId }) => {
    const [dashboardData, setDashboardData] = useState({});
    const [error, setError] = useState('');

    useEffect(() => {
        const fetchDashboardData = async () => {
            try {
                const response = await axios.get('/api/dashboard', { params: { user_id: userId }});
                setDashboardData(response.data);
            } catch (err) {
                setError('Error fetching dashboard data');
            }
        };
        fetchDashboardData();
    }, [userId]);

    if (error) {
        return <p>{error}</p>;
    }

    if (!dashboardData.user_profile) {
        return <p>User profile data missing</p>;
    }

    return (
        <div>
            <h1>Welcome, {dashboardData.user_profile.name}</h1>
            <div>
                <h2>Banking Products</h2>
                {dashboardData.banking_products.map(product => (
                    <div key={product.id}>
                        <h3>{product.name}</h3>
                        <p>{product.description}</p>
                    </div>
                ))}
            </div>
            <div>
                <h2>Services</h2>
                {dashboardData.services.map(service => (
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