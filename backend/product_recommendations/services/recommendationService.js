// Epic Title: Implement Product Recommendations Based on User Preferences

const { pool } = require('../../database/pool');

const getRecommendations = async (userId) => {
  // Query to fetch user browsing and purchase history
  const result = await pool.query(`
    SELECT p.id, p.name, p.description, p.price
    FROM products p
    JOIN browsing_history bh ON p.id = bh.product_id
    JOIN purchase_history ph ON p.id = ph.product_id
    WHERE bh.user_id = $1 OR ph.user_id = $1
    LIMIT 10
  `, [userId]);
  return result.rows;
};

module.exports = { getRecommendations };