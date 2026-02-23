// Epic Title: Implement Backend Endpoints Using Node.js for Admin Dashboard

const express = require('express');
const cors = require('cors');
const helmet = require('helmet');
const morgan = require('morgan');
const adminRouter = require('./admin_dashboard/controllers/adminController');

const app = express();

// Middleware
app.use(cors());
app.use(helmet());
app.use(morgan('dev'));
app.use(express.json());

// Routes
app.use('/api/admin', adminRouter);

const PORT = process.env.PORT || 3000;

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});