# Epic Title: Real-time Status Updates Using React and Redis

import React, { useEffect, useState } from 'react';
import io from 'socket.io-client';

const socket = io('http://localhost:5000');

const StatusTracker = () => {
  const [status, setStatus] = useState('');

  useEffect(() => {
    socket.on('status_update', (data) => {
      setStatus(data.status);
    });

    return () => {
      socket.off('status_update');
    };
  }, []);

  return (
    <div>
      <h1>Status Tracker</h1>
      <p>Current Status: {status}</p>
    </div>
  );
};

export default StatusTracker;