// Epic Title: Develop Admin Dashboard Interface Using Next.js

import React from 'react';
import Link from 'next/link';

const Sidebar = () => {
  return (
    <aside className="sidebar">
      <ul>
        <li>
          <Link href="/orders">
            <a>Order Management</a>
          </Link>
        </li>
        <li>
          <Link href="/products">
            <a>Product Listings</a>
          </Link>
        </li>
        <li>
          <Link href="/analytics">
            <a>Analytics & Reporting</a>
          </Link>
        </li>
        <li>
          <Link href="/reviews">
            <a>Reviews & Ratings</a>
          </Link>
        </li>
      </ul>
    </aside>
  );
};

export default Sidebar;