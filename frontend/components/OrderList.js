// Epic Title: Implement Frontend with Next.js

import React from 'react';
import formatDate from '../utils/formatDate';

const OrderList = ({ orders }) => {
  return (
    <ul>
      {orders.map(order => (
        <li key={order.id}>
          <p>Order ID: {order.id}</p>
          <p>Status: {order.status.status}</p>
          <p>Date: {formatDate(order.date)}</p>
          <ul>
            {order.items.map(item => (
              <li key={item.product_id}>
                <p>Product ID: {item.product_id}</p>
                <p>Quantity: {item.quantity}</p>
                <p>Price: ${item.price}</p>
              </li>
            ))}
          </ul>
        </li>
      ))}
    </ul>
  );
};

export default OrderList;