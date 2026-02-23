// Epic Title: Develop Admin Dashboard Interface Using Next.js

import React from 'react';
import Head from 'next/head';
import '../styles/globals.css';

function MyApp({ Component, pageProps }) {
  return (
    <>
      <Head>
        <title>Admin Dashboard</title>
      </Head>
      <Component {...pageProps} />
    </>
  );
}

export default MyApp;