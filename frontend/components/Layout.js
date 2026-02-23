// Epic Title: Develop Admin Dashboard Interface Using Next.js

import React from 'react';
import Navbar from './Navbar';
import Sidebar from './Sidebar';

const Layout = ({ children }) => {
  return (
    <div className="layout">
      <Navbar />
      <Sidebar />
      <main className="content">{children}</main>
    </div>
  );
};

export default Layout;