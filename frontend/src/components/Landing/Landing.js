import React from 'react';
import { Typography, Box, Paper } from '@mui/material';
import SearchBar from '../SearchBar/SearchBar';
import { Link } from 'react-router-dom';

function Landing() {

  return (
    <Box 
      mt='35vh' mb='6vh'
    >
      <Paper sx={{padding: '2rem'}}>
        <Link to="/" style={{ textDecoration: 'none', color: 'inherit' }}>
          <Typography variant="h2" gutterBottom mb='3vh' sx={{ fontFamily: 'MinecraftEvenings', textAlign: 'center' }}>
          <b>Q U E R Y&nbsp;&nbsp;&nbsp;C R A F T E R</b>
          </Typography>
        </Link>
        <SearchBar initialQuery=''/>
      </Paper>
    </Box>
  );
}

export default Landing;
