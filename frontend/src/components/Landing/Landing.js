import React, { useState } from 'react';
import { Typography, Box, IconButton, OutlinedInput, FormControl } from '@mui/material';
import SearchIcon from '@mui/icons-material/Search';

function Landing() {
  const [query, setQuery] = useState('')
  const queryDestLink = `/search?query=${query}`

  return (
    <Box 
      sx={{ mt: '25vh', mb: 4}}
    >
      <Typography variant="h4" fullWidth gutterBottom>
        Crafter Engine
      </Typography>
      <Box display="flex" flexDirection="row" alignItems="center" mt='3vh' gap={2}>
        <FormControl fullWidth variant="outlined">
          <OutlinedInput fullWidth
            id="search-box"
            variant="outlined"
            value={query}
            onChange={event => {
              setQuery(event.target.value);
            }}
            onKeyUp={(event) => {
              if (event.key === 'Enter') {
                window.location.href = queryDestLink;
              }
            }}
          />
        </FormControl>
        <IconButton 
          variant="contained" 
          color="primary" 
          href={queryDestLink}
        >
          <SearchIcon />
        </IconButton>
      </Box>
    </Box>
  );
}

export default Landing;
