import { Box, FormControl, IconButton, OutlinedInput } from '@mui/material';
import React, { useState } from 'react'
import SearchIcon from '@mui/icons-material/Search';

function SearchBar() {
  const [query, setQuery] = useState('')
  const queryDestLink = `/search?query=${query}`
  return (
    <Box display="flex" flexDirection="row" alignItems="center" gap={2}>
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
  )
}

export default SearchBar