// Epic Title: Implement Backend Endpoints Using Node.js for Admin Dashboard

const express = require('express');
const router = express.Router();
const { getOrderStats, getProductStats } = require('../services/adminService');

// GET admin dashboard statistics
router.get('/stats', async (req, res) => {
  try {
    const orderStats = await getOrderStats();
    const productStats = await getProductStats();
    res.status(200).json({ orderStats, productStats });
  } catch (error) {
    res.status(500).json({ error: 'Failed to fetch statistics' });
  }
});

module.exports = router;