# Epic Title: Implement Backend Endpoints Using Node.js for Admin Dashboard

const { DataTypes } = require('sequelize');
const { sequelize } = require('../../database/sequelize');

const Admin = sequelize.define('Admin', {
  id: {
    type: DataTypes.INTEGER,
    primaryKey: true,
    autoIncrement: true,
    allowNull: false,
  },
  username: {
    type: DataTypes.STRING,
    allowNull: false,
  },
  password: {
    type: DataTypes.STRING,
    allowNull: false,
  },
});

module.exports = Admin;