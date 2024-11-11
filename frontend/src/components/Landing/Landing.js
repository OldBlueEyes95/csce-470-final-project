import React from 'react';
import { Typography, Box, Paper } from '@mui/material';
import SearchBar from '../SearchBar/SearchBar';

function Landing() {

  return (
    <Box 
      mt='35vh' mb='6vh'
    >
      <Paper sx={{padding: '2rem'}}>
        <Typography variant="h4" gutterBottom mb='3vh'>
          Crafter Engine
        </Typography>
        <SearchBar initialQuery=''/>
      </Paper>
    </Box>
  );
}

export default Landing;
