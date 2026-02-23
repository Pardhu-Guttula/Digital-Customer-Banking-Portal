// Epic Title: Backend Data Aggregation Using Node.js

const express = require('express');
const router = express.Router();
const { aggregateData } = require('../services/data_service');

router.get('/aggregate', async (req, res) => {
  try {
    const data = await aggregateData();
    res.status(200).json(data);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

module.exports = router;