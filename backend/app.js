// Epic Title: Backend Data Aggregation Using Node.js

const express = require('express');
const mongoose = require('mongoose');
const dataController = require('./data_aggregation/controllers/data_controller');

const app = express();
const DATABASE_URL = 'mongodb://localhost:27017/mydatabase';

mongoose.connect(DATABASE_URL, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

app.use('/api/data', dataController);

app.get('/', (req, res) => {
  res.send('Hello World!');
});

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});