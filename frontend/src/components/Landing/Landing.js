import React from 'react';
import { Typography, Box } from '@mui/material';

function Landing() {
  return (
    <Box 
      sx={{ mt: 4, mb: 4, height: '100px' }}
    >
      <Typography variant="h4" gutterBottom>
        Landing Page
      </Typography>
      <Typography variant="body1">
        This is the landing page. Add your search bar and components here.
      </Typography>
    </Box>
  );
}

export default Landing;
