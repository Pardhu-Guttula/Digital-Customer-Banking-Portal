// Epic Title: Implement Frontend with Next.js

import React, { useEffect, useState } from 'react';
import axios from 'axios';
import OrderList from '../components/OrderList';

const Orders = () => {
  const [orders, setOrders] = useState([]);

  useEffect(() => {
    async function fetchOrders() {
      try {
        const response = await axios.get('http://localhost:5000/view-orders/1');
        setOrders(response.data);
      } catch (error) {
        console.error('Error fetching orders:', error);
      }
    }

    fetchOrders();
  }, []);

  return (
    <div>
      <h1>My Orders</h1>
      <OrderList orders={orders} />
    </div>
  );
};

export default Orders;