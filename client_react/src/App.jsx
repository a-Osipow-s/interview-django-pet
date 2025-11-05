import React, { useState, useEffect } from 'react';
import { Container, Box } from '@mui/material';
import PersonTables from './PersonTables.jsx';

export default function TabbedTables() {
  const [activeTab, setActiveTab] = useState(0);

  const handleTabChange = (event, newValue) => {
    setActiveTab(newValue);
  };

  return (
    <Container fixed>
      <Box sx={{ width: '100%', p: 3, boxSizing: 'border-box' }}>
        <PersonTables />
      </Box>
    </Container>
  );
}