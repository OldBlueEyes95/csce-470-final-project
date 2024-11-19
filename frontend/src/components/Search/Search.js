import React, { useEffect, useState } from 'react';
import { Typography, Box, CircularProgress, Paper } from '@mui/material';
import { Link, useSearchParams } from 'react-router-dom';
import Hit from '../Hit/Hit';
import SearchBar from '../SearchBar/SearchBar';
import { fetchSearchResults } from '../../api/searchApi';
import ErrorOutlineIcon from '@mui/icons-material/ErrorOutline';

function Search() {
  const [searchParams] = useSearchParams();
  const query = searchParams.get('query');
  const [hits, setHits] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

    useEffect(() => {
      if (!query) {
        console.log('No query parameter found')
      }
      fetchSearchResults(query)
        .then((results) => {
          console.log("API response:", results); // Debugging line
          if (!results || results.length <= 0) {
            setLoading(false);
            setError('No Pages Found');
            console.error('No Pages Found', results);
            return;
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
          setLoading(false);
        })
        .catch((err) => {
          setLoading(false);
          
          if (err.response) {
            // Server responded with a status other than 200 range
            if (err.response.status === 404) {
              setError('No results found. Please try a different query.');
            } else if (err.response.status >= 500) {
              setError('Server error. Please try again later.');
            } else {
              setError('Unexpected error occurred. Please try again.');
            }
            console.error(`HTTP Error: ${err.response.status}`, err.response.data);
          } else if (err.request) {
            // Request was made but no response was received
            setError('Network error. Please check your connection.');
            console.error('Network Error:', err.request);
          } else {
            // Something else happened
            setError('An unexpected error occurred. Please try again.');
            console.error('Error:', err.message);
          }
        });
    }, [query]);

  return (
    <Paper 
      elevation={3} 
      sx={{ 
        borderRadius: 0, // Square edges
        minHeight: '100vh', // Full page height
        padding: 4, // Add padding to keep content from touching the edges
        boxSizing: 'border-box' // Ensure padding doesn't affect height calculation
      }}
    >
      <Link to="/" style={{ textDecoration: 'none', color: 'inherit' }}>
        <Typography variant="h5" gutterBottom sx={{ fontFamily: 'MinecraftEvenings' }}>
          <b>Q U E R Y&nbsp;&nbsp;&nbsp;C R A F T E R</b>
        </Typography>
      </Link>
      <SearchBar initialQuery={query} />

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
    </Paper>
  );
}

export default Search;
