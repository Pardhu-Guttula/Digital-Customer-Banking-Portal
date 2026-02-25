# Epic Title: Develop a Feature in React for Users to Access Interaction History

import React, { useState, useEffect } from 'react';
import axios from 'axios';

const InteractionHistory = () => {
  const [interactions, setInteractions] = useState([]);
  const userId = 1; // Placeholder for authenticated user ID

  useEffect(() => {
    const fetchInteractions = async () => {
      try {
        const response = await axios.get(`/api/interactions/${userId}`);
        setInteractions(response.data);
      } catch (error) {
        console.error("Error fetching interaction history:", error);
      }
    };

    fetchInteractions();
  }, [userId]);

  return (
    <div>
      <h1>Interaction History</h1>
      <ul>
        {interactions.map((interaction, index) => (
          <li key={index}>
            <p>Type: {interaction.interaction_type}</p>
            <p>Data: {JSON.stringify(interaction.interaction_data)}</p>
            <p>Date: {interaction.created_at}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default InteractionHistory;