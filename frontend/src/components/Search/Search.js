import React, { useEffect, useState } from 'react';
import { Typography, Box, CircularProgress } from '@mui/material';
import { useSearchParams } from 'react-router-dom';
import Hit from '../Hit/Hit';
import SearchBar from '../SearchBar/SearchBar';
import { fetchSearchResults } from '../../api/searchApi';
import ErrorOutlineIcon from '@mui/icons-material/ErrorOutline';

function Search() {
  const [searchParams] = useSearchParams();
  const query = searchParams.get('query');
  const [hits, setHits] = useState([]);
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState('')

    useEffect(() => {
      if (!query) {
        console.log('No query parameter found')
      }
      fetchSearchResults(query)
        .then((results) => {
          if (results.length <= 0) {
            setLoading(false)
            setError('No Pages Found')
            console.error('No Pages Found', results)
          }

          const hitComponents = results.map((result, index) => (
            <Hit
              key={index}
              title={result.title}
              text={result.text}
              link={result.link}
            />
          ));
          setHits(hitComponents);
          setLoading(false)
        })
        .catch((err) => {
          setLoading(false)
          setError('Error fetching results')
          console.error('Error fetching results:', err);
        });
    }, [query]);

  return (
    <Box sx={{ mt: 4 }}>
      <Typography variant="h5" gutterBottom>
        Crafter Engine
      </Typography>
      <SearchBar initialQuery={query}/>
      {!query && <Typography variant="body1">No query parameter provided</Typography>}
      {!(loading || error) && <Box marginTop='3vh'>
        {hits.length > 0 ? hits.map((hit, index) => (
          <Box key={index} sx={{ mb: 2 }}>
            {hit}
          </Box>
        )) : (
          <Typography>{error}</Typography>
        )}
      </Box>}
      {(loading || error) && <Box
        sx={{
          maxWidth: '100%',
          marginTop: '30vh',
          display: 'flex',
          justifyContent: 'center',
          alignItems: 'center',
          flexDirection: 'column'
        }}
      >
        {(loading && !error) && <CircularProgress size={80} />}
        {error && (
          <>
            <ErrorOutlineIcon color="error" sx={{ fontSize: 80 }} />
            <Typography variant="h6" color="error" marginTop='2vh'>
              {error}
            </Typography>
          </>
        )}
      </Box>}
    </Box>
  );
}

export default Search;
