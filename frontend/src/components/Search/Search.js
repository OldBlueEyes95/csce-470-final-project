import React, { useEffect, useState } from 'react';
import { Typography, Box } from '@mui/material';
import { useSearchParams } from 'react-router-dom';
import Hit from '../Hit/Hit';
import SearchBar from '../SearchBar/SearchBar';

function Search() {
  const [searchParams] = useSearchParams();
  const query = searchParams.get('query');
  const [hits, setHits] = useState([]);

  useEffect(() => {
    // Simulate a data fetching or creation process for `hits`
    if (query) {
      // Replace this logic with an actual data fetching or processing function
      const simulatedHits = Array.from({ length: query.length }, (_, index) => (
        <Hit key={index} title={`Hit ${index + 1}`} text={`Hit ${index + 1} for query: ${query}`} link={`https://minecraft.wiki/`} />
      ));
      setHits(simulatedHits);
    }
  }, [query]);

  return (
    <Box sx={{ mt: 4 }}>
      <Typography variant="h4" gutterBottom>
        Search Result Page
      </Typography>
      <SearchBar initialQuery={query}/>
      <Typography variant="body1">
        {query ? '' : 'No query parameter provided.'}
      </Typography>
      <Box marginTop='3vh'>
        {hits.length > 0 ? hits.map((hit, index) => (
          <Box key={index} sx={{ mb: 2 }}>
            {hit}
          </Box>
        )) : (
          <Typography>No results found.</Typography>
        )}
      </Box>
    </Box>
  );
}

export default Search;
