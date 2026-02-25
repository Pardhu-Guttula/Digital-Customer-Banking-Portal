# Epic Title: React UI for Service Modification Requests

import React, { useState } from 'react';

const ServiceModificationForm = () => {
  const [formData, setFormData] = useState({
    service_name: '',
    modification_details: '',
  });
  const [errors, setErrors] = useState({});
  const [message, setMessage] = useState('');

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const validationErrors = validate(formData);
    if (Object.keys(validationErrors).length === 0) {
      try {
        const response = await fetch('/service_modification', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(formData),
        });
        const data = await response.json();
        if (response.ok) {
          setMessage(data.message);
        } else {
          setMessage(data.error);
        }
      } catch (error) {
        console.error('Error submitting form:', error);
        setMessage('Internal server error. Please try again later.');
      }
    } else {
      setErrors(validationErrors);
    }
  };

  const validate = (values) => {
    const errors = {};
    if (!values.service_name) errors.service_name = 'Service name is required';
    if (!values.modification_details) errors.modification_details = 'Modification details are required';
    return errors;
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label>Service Name</label>
        <input type="text" name="service_name" value={formData.service_name} onChange={handleChange} />
        {errors.service_name && <span>{errors.service_name}</span>}
      </div>
      <div>
        <label>Modification Details</label>
        <input type="text" name="modification_details" value={formData.modification_details} onChange={handleChange} />
        {errors.modification_details && <span>{errors.modification_details}</span>}
      </div>
      <button type="submit">Submit</button>
      {message && <div>{message}</div>}
    </form>
  );
};

export default ServiceModificationForm;