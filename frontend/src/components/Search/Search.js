import React from 'react';
import { Typography, Box } from '@mui/material';
import { useSearchParams } from 'react-router-dom';

function Results() {
  const [searchParams] = useSearchParams();
  const query = searchParams.get('query');

  return (
    <Box sx={{ mt: 4 }}>
      <Typography variant="h4" gutterBottom>
        Results Page
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
    </Box>
  );
}

export default Results;
