# Epic Title: Dashboard Backend Data Integration

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