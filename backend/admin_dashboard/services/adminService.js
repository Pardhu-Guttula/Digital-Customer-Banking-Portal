// Epic Title: Implement Backend Endpoints Using Node.js for Admin Dashboard

const { pool } = require('../../database/pool');

const getOrderStats = async () => {
  const stats = await pool.query('SELECT COUNT(*) AS total_orders, SUM(total_amount) AS total_revenue FROM orders');
  return stats.rows[0];
};

const getProductStats = async () => {
  const stats = await pool.query('SELECT COUNT(*) AS total_products FROM products');
  return stats.rows[0];
};

module.exports = { getOrderStats, getProductStats };