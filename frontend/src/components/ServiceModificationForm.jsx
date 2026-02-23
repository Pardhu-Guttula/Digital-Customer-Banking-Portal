# Epic Title: Develop streamlined workflows for submitting service modification requests

import React, { useState } from 'react';
import axios from 'axios';

const ServiceModificationForm = () => {
    const [formData, setFormData] = useState({
        service_name: '',
        modification_details: '',
        user_id: 'user123'  // Hardcoded for the example
    });
    const [error, setError] = useState('');
    const [successMessage, setSuccessMessage] = useState('');

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData({
            ...formData,
            [name]: value
        });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post('/api/service/modify', formData);
            setSuccessMessage(response.data.message);
            setError('');
        } catch (err) {
            setError(err.response.data.error);
            setSuccessMessage('');
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <div>
                <label>Service Name:</label>
                <input type="text" name="service_name" value={formData.service_name} onChange={handleChange} />
            </div>
            <div>
                <label>Modification Details:</label>
                <input type="text" name="modification_details" value={formData.modification_details} onChange={handleChange} />
            </div>
            <button type="submit">Submit</button>
            {error && <p style={{ color: 'red' }}>{error}</p>}
            {successMessage && <p style={{ color: 'green' }}>{successMessage}</p>}
        </form>
    );
};

export default ServiceModificationForm;