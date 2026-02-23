# Epic Title: Data Visualization Using Next.js

import { useEffect, useState } from 'react';
import dynamic from 'next/dynamic';

const Chart = dynamic(() => import('react-apexcharts'), { ssr: false });

const Dashboard = () => {
  const [salesData, setSalesData] = useState([]);
  const [behaviorData, setBehaviorData] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function fetchData() {
      const salesResponse = await fetch('/api/reports/sales');
      const behaviorResponse = await fetch('/api/reports/behavior');
      const salesData = await salesResponse.json();
      const behaviorData = await behaviorResponse.json();
      setSalesData(salesData);
      setBehaviorData(behaviorData);
      setLoading(false);
    }
    fetchData();
  }, []);

  if (loading) {
    return <p>Loading...</p>;
  }

  return (
    <div>
      <h1>Dashboard</h1>
      <div style={{ display: 'flex', justifyContent: 'space-around' }}>
        <div>
          <h2>Sales Data</h2>
          <Chart options={salesData.options} series={salesData.series} type="bar" height={350} />
        </div>
        <div>
          <h2>User Behavior Data</h2>
          <Chart options={behaviorData.options} series={behaviorData.series} type="line" height={350} />
        </div>
      </div>
    </div>
  );
};

export default Dashboard;