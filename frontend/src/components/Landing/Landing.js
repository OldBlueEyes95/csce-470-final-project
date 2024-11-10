import React from 'react';
import { Typography, Box } from '@mui/material';
import SearchBar from '../SearchBar/SearchBar';

function Landing() {

  return (
    <Box 
      mt='25vh' mb='6vh'
    >
      <Typography variant="h4" fullWidth gutterBottom mb='3vh'>
        Crafter Engine
      </Typography>
      <SearchBar initialQuery=''/>
    </Box>
  );
}

export default Landing;
