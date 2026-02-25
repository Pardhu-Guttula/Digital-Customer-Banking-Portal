# Epic Title: Develop Document Upload Capability Using React

import React, { useState } from 'react';

const DocumentUpload = () => {
  const [file, setFile] = useState(null);
  const [message, setMessage] = useState('');

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleUpload = async () => {
    if (!file) {
      setMessage('Please select a file first.');
      return;
    }

    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await fetch('/api/documents/upload', {
        method: 'POST',
        body: formData
      });

      if (response.ok) {
        setMessage('Document uploaded successfully.');
      } else {
        const errorData = await response.json();
        setMessage(`Upload failed: ${errorData.detail}`);
      }
    } catch (error) {
      setMessage(`Upload failed: ${error.message}`);
    }
  };

  const handleCancel = () => {
    setFile(null);
    setMessage('File upload cancelled.');
  };

  return (
    <div>
      <h1>Document Upload</h1>
      <input type="file" onChange={handleFileChange} />
      <button onClick={handleUpload}>Upload</button>
      <button onClick={handleCancel}>Cancel</button>
      {message && <p>{message}</p>}
    </div>
  );
};

export default DocumentUpload;