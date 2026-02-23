# Epic Title: Implement user interface using React

import React, { useState } from 'react';

const WorkflowForm = () => {
    const [formData, setFormData] = useState({
        name: '',
        email: '',
        phone: '',
        request: ''
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

    const validateForm = () => {
        if (!formData.name || !formData.email || !formData.phone || !formData.request) {
            setError('All fields are mandatory');
            return false;
        }
        return true;
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        if (!validateForm()) return;
        
        try {
            const response = await fetch('/api/workflow/submit', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(formData)
            });

            const result = await response.json();
            if (response.ok) {
                setSuccessMessage(result.message);
                setError('');
            } else {
                setError(result.error);
                setSuccessMessage('');
            }
        } catch (err) {
            setError('Failed to submit request');
            setSuccessMessage('');
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <div>
                <label>Name:</label>
                <input type="text" name="name" value={formData.name} onChange={handleChange} />
            </div>
            <div>
                <label>Email:</label>
                <input type="email" name="email" value={formData.email} onChange={handleChange} />
            </div>
            <div>
                <label>Phone:</label>
                <input type="text" name="phone" value={formData.phone} onChange={handleChange} />
            </div>
            <div>
                <label>Request:</label>
                <textarea name="request" value={formData.request} onChange={handleChange} />
            </div>
            <button type="submit">Submit</button>
            {error && <p style={{ color: 'red' }}>{error}</p>}
            {successMessage && <p style={{ color: 'green' }}>{successMessage}</p>}
        </form>
    );
};

export default WorkflowForm;