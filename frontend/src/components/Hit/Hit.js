import React from 'react';
import { Typography, Box, useTheme, Link } from '@mui/material';
import OpenInNewIcon from '@mui/icons-material/OpenInNew';

function Hit({ title, link, text }) {
  const theme = useTheme();
  return (
    <Box 
      sx={{ 
        padding: '12px 16px', 
        borderBottom: '1px solid #e0e0e0',
        '&:hover': { backgroundColor: theme.palette.action.hover } 
      }}
    >
      <Link 
        href={link} 
        color="primary" 
        underline="hover" 
        variant="h6" 
        display='inline-flex'
        alignItems='center'
        fontSize='24'
      >
        {title}
        <OpenInNewIcon fontSize='inherit' sx={{marginLeft: '6px'}} />
      </Link>
      <Typography 
        variant="body2" 
        color="text.secondary" 
        sx={{ marginTop: '4px' }}
      >
        {link}
      </Typography>
      <Typography 
        variant="body2" 
        color="text.primary" 
        sx={{ marginTop: '6px' }}
      >
        {text}
      </Typography>
    </Box>
  );
}

export default Hit;
