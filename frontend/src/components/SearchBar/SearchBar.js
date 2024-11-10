import { Box, FormControl, FormHelperText, IconButton, InputAdornment, OutlinedInput } from '@mui/material';
import React, { useState } from 'react'
import SearchIcon from '@mui/icons-material/Search';

function SearchBar({ initialQuery }) {
  const [query, setQuery] = useState(initialQuery)
  const queryDestLink = `/search?query=${encodeURIComponent(query)}`
  const [error, setError] = useState('');

  const handleSearch = () => {
    if (query.trim()) {
      setError('');
      window.location.href = queryDestLink;
    } else {
      setError('Please enter a valid search query');
    }
  };

  return (
    <Box display='flex' flexDirection='row' alignItems='center' gap={2}>
      <FormControl fullWidth variant='outlined'>
        <OutlinedInput
          id='search-box'
          variant='outlined'
          value={query}
          onChange={(event) => {
            setQuery(event.target.value);
            if (event.target.value.trim()) {
              setError('');
            }
          }}
          onKeyUp={(event) => {
            if (event.key === 'Enter') {
              handleSearch();
            }
          }}
          endAdornment={
            <InputAdornment position="end">
              <IconButton
                color="primary"
                onClick={handleSearch}
                edge="end"
              >
                <SearchIcon />
              </IconButton>
            </InputAdornment>
          }
        />
        {error && (
          <FormHelperText>
            {error}
          </FormHelperText>
        )}
      </FormControl>
    </Box>
  )
}

export default SearchBar