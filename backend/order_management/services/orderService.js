// Epic Title: Implement Backend with Node.js

const { Pool } = require('pg');
const pool = new Pool({
  user: 'user',
  host: 'localhost',
  database: 'mydatabase',
  password: 'password',
  port: 5432,
});

// Service methods
const getAllOrders = async () => {
  const result = await pool.query('SELECT * FROM orders');
  return result.rows;
};

const getOrderById = async (id) => {
  const result = await pool.query('SELECT * FROM orders WHERE id = $1', [id]);
  return result.rows[0];
};

const createOrder = async (order) => {
  const result = await pool.query(
    'INSERT INTO orders (user_id, address_id, total_amount, status_id, date) VALUES ($1, $2, $3, $4, $5) RETURNING *',
    [order.user_id, order.address_id, order.total_amount, order.status_id, order.date]
  );
  return result.rows[0];
};

const updateOrder = async (id, order) => {
  const result = await pool.query(
    'UPDATE orders SET user_id = $1, address_id = $2, total_amount = $3, status_id = $4, date = $5 WHERE id = $6 RETURNING *',
    [order.user_id, order.address_id, order.total_amount, order.status_id, order.date, id]
  );
  return result.rows[0];
};

const deleteOrder = async (id) => {
  const result = await pool.query('DELETE FROM orders WHERE id = $1', [id]);
  return result.rowCount > 0;
};

module.exports = {
  getAllOrders,
  getOrderById,
  createOrder,
  updateOrder,
  deleteOrder,
};