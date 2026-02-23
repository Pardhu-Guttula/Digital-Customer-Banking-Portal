// Epic Title: Implement Frontend with Next.js

import React from 'react';
import Link from 'next/link';

const Home = () => {
  return (
    <div>
      <h1>Welcome to the Next.js App</h1>
      <nav>
        <ul>
          <li>
            <Link href="/orders">
              <a>View Orders</a>
            </Link>
          </li>
        </ul>
      </nav>
    </div>
  );
};

export default Home;