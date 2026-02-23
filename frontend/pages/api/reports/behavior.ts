# Epic Title: Data Visualization Using Next.js

import { NextApiRequest, NextApiResponse } from 'next';

export default async (req: NextApiRequest, res: NextApiResponse) => {
  const response = await fetch('http://localhost:5000/api/insights/generate');
  const data = await response.json();
  const transformedData = transformBehaviorData(data);
  
  res.status(200).json(transformedData);
};

const transformBehaviorData = (data: any) => {
  return {
    options: {
      chart: {
        id: 'behavior-data-chart'
      },
      xaxis: {
        categories: Object.keys(data.common_actions)
      }
    },
    series: [{
      name: 'User Actions',
      data: Object.values(data.common_actions)
    }]
  };
};