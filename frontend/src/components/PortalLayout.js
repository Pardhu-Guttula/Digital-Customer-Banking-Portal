# Epic Title: Develop Responsive Design for the Portal Using React

import React from 'react';
import './PortalLayout.css';

const PortalLayout = () => {
  return (
    <div className="portal-layout">
      <header className="header">
        <h1>Responsive Portal</h1>
      </header>
      <main className="main-content">
        <p>Welcome to the portal. This layout adjusts based on screen size!</p>
      </main>
      <footer className="footer">
        <p>&copy; 2023 Responsive Portal</p>
      </footer>
    </div>
  );
};

export default PortalLayout;