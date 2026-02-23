// Epic Title: Implement Product Recommendations Based on User Preferences

const express = require('express');
const router = express.Router();
const { getRecommendations } = require('../services/recommendationService');

// GET personalized recommendations
router.get('/:userId', async (req, res) => {
  const { userId } = req.params;
  try {
    const recommendations = await getRecommendations(userId);
    res.status(200).json(recommendations);
  } catch (error) {
    res.status(500).json({ error: 'Failed to fetch recommendations' });
  }
});

module.exports = router;