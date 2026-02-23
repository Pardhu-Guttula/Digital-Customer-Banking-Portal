# Epic Title: Implement Backend Endpoints Using Node.js for Admin Dashboard

const { Sequelize } = require('sequelize');

const sequelize = new Sequelize('mydatabase', 'user', 'password', {
  host: 'localhost',
  dialect: 'postgres',
});

sequelize.authenticate()
  .then(() => console.log('Connected to PostgreSQL using Sequelize'))
  .catch(err => console.error('Connection error', err));

module.exports = { sequelize };