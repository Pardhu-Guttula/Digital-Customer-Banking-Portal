// Epic Title: Implement Product Recommendations Based on User Preferences

const express = require('express');
const cors = require('cors');
const helmet = require('helmet');
const morgan = require('morgan');
const recommendationRouter = require('./product_recommendations/controllers/recommendationController');

const app = express();

// Middleware
app.use(cors());
app.use(helmet());
app.use(morgan('dev'));
app.use(express.json());

// Routes
app.use('/api/recommendations', recommendationRouter);

const PORT = process.env.PORT || 3000;

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});