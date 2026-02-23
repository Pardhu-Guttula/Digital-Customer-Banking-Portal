# Epic Title: Dynamic and Interactive Dashboard UI using React

import React from 'react';
import Dashboard from './Dashboard';

const App = () => {
    const userId = 'user123';

    return (
        <div>
            <h1>Banking Dashboard</h1>
            <Dashboard userId={userId} />
        </div>
    );
};

export default App;