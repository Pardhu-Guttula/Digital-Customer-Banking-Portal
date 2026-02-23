# Epic Title: Data Visualization Using Next.js

import { NextApiRequest, NextApiResponse } from 'next';

export default async (req: NextApiRequest, res: NextApiResponse) => {
  const response = await fetch('http://localhost:5000/api/reports/generate');
  const data = await response.json();
  const transformedData = transformSalesData(data);
  
  res.status(200).json(transformedData);
};

const transformSalesData = (data: any) => {
  return {
    options: {
      chart: {
        id: 'sales-data-chart'
      },
      xaxis: {
        categories: data.sales.map((item: any) => item.date)
      }
    },
    series: [{
      name: 'Sales',
      data: data.sales.map((item: any) => item.total_revenue)
    }]
  };
};