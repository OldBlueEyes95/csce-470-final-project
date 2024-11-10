import React, { useEffect, useState } from 'react';
import { Typography, Box } from '@mui/material';
import { useSearchParams } from 'react-router-dom';
import Hit from '../Hit/Hit';

function Search() {
  const [searchParams] = useSearchParams();
  const query = searchParams.get('query');
  const [hits, setHits] = useState([]);

  useEffect(() => {
    // Simulate a data fetching or creation process for `hits`
    if (query) {
      // Replace this logic with an actual data fetching or processing function
      const simulatedHits = Array.from({ length: query.length }, (_, index) => (
        <Hit key={index} content={`Hit ${index + 1} for query: ${query}`} />
      ));
      setHits(simulatedHits);
    }
  }, [query]);

  return (
    <Box sx={{ mt: 4 }}>
      <Typography variant="h4" gutterBottom>
        Search Result Page
      </Typography>
      <Typography variant="body1">
        {query ? (
          <>
            The query parameter is: <strong>{query}</strong>
          </>
        ) : (
          'No query parameter provided.'
        )}
      </Typography>
      {hits.length > 0 ? hits.map((hit, index) => (
        <Box key={index} sx={{ mb: 2 }}>
          {hit}
        </Box>
      )) : (
        <Typography>No results found.</Typography>
      )}
    </Box>
  );
}

export default Search;
