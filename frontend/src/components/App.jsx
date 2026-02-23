# Epic Title: Personalized Dashboard Layout

import React from 'react';
import Dashboard from './Dashboard';

const App = () => {
    const userId = 'user123'; // Simulate logged in user

    return (
        <div>
            <h1>Banking Dashboard</h1>
            <Dashboard userId={userId} />
        </div>
    );
};

export default App;