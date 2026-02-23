// Epic Title: Backend Data Aggregation Using Node.js

const axios = require('axios');
const DataSource = require('../models/data_source');

async function aggregateData() {
  const sources = await DataSource.find();
  const dataPromises = sources.map(source => fetchDataFromSource(source));

  const allData = await Promise.all(dataPromises);
  return preprocessData(allData);
}

async function fetchDataFromSource(source) {
  try {
    const response = await axios.get(source.url);
    return response.data;
  } catch (error) {
    throw new Error(`Failed to fetch data from source: ${source.name}`);
  }
}

function preprocessData(dataArray) {
  // Implement your data preprocessing logic here
  return dataArray.reduce((acc, data) => acc.concat(data), []);
}

module.exports = {
  aggregateData,
};