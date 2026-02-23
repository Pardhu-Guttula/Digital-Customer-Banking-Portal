// Epic Title: Implement Backend with Node.js

const express = require('express');
const router = express.Router();
const orderService = require('../services/orderService');

// GET all orders
router.get('/', async (req, res) => {
  try {
    const orders = await orderService.getAllOrders();
    res.status(200).json(orders);
  } catch (error) {
    res.status(500).json({ error: 'Failed to get orders' });
  }
});

// GET order by ID
router.get('/:id', async (req, res) => {
  const { id } = req.params;
  try {
    const order = await orderService.getOrderById(id);
    if (order) {
      res.status(200).json(order);
    } else {
      res.status(404).json({ error: 'Order not found' });
    }
  } catch (error) {
    res.status(500).json({ error: 'Failed to get order' });
  }
});

// POST create new order
router.post('/', async (req, res) => {
  const newOrder = req.body;
  try {
    const order = await orderService.createOrder(newOrder);
    res.status(201).json(order);
  } catch (error) {
    res.status(500).json({ error: 'Failed to create order' });
  }
});

// PUT update order
router.put('/:id', async (req, res) => {
  const { id } = req.params;
  const updatedOrder = req.body;
  try {
    const order = await orderService.updateOrder(id, updatedOrder);
    if (order) {
      res.status(200).json(order);
    } else {
      res.status(404).json({ error: 'Order not found' });
    }
  } catch (error) {
    res.status(500).json({ error: 'Failed to update order' });
  }
});

// DELETE order
router.delete('/:id', async (req, res) => {
  const { id } = req.params;
  try {
    const result = await orderService.deleteOrder(id);
    if (result) {
      res.status(200).json({ message: 'Order deleted successfully' });
    } else {
      res.status(404).json({ error: 'Order not found' });
    }
  } catch (error) {
    res.status(500).json({ error: 'Failed to delete order' });
  }
});

module.exports = router;