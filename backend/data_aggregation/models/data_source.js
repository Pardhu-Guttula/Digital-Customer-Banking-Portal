// Epic Title: Backend Data Aggregation Using Node.js

const mongoose = require('mongoose');

const DataSourceSchema = new mongoose.Schema({
  name: {
    type: String,
    required: true,
  },
  url: {
    type: String,
    required: true,
  },
  type: {
    type: String,
    required: true,
  },
});

module.exports = mongoose.model('DataSource', DataSourceSchema);