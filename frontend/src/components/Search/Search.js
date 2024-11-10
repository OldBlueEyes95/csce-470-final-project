import React, { useEffect, useState } from 'react';
import { Typography, Box } from '@mui/material';
import { useSearchParams } from 'react-router-dom';
import Hit from '../Hit/Hit';
import SearchBar from '../SearchBar/SearchBar';
import { fetchSearchResults } from '../../api/Interface/searchApi';

function Search() {
  const [searchParams] = useSearchParams();
  const query = searchParams.get('query');
  const [hits, setHits] = useState([]);
  const [noHitMessage, setNoHitMessage] = useState('Loading...')

    useEffect(() => {
      if (!query) {
        console.log('No query parameter found')
      }
      fetchSearchResults(query)
        .then((results) => {
          // Map the results to Hit components
          const hitComponents = results.map((result, index) => (
            <Hit
              key={index}
              title={result.title}
              text={result.text}
              link={result.link}
            />
          ));
          setHits(hitComponents);
        })
        .catch((err) => {
          setNoHitMessage('Error fetching results:')
          console.error('Error fetching results:', err);
        });
    }, [query]);

  return (
    <Box sx={{ mt: 4 }}>
      <Typography variant="h5" gutterBottom>
        Crafter Engine
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
          <Typography>{noHitMessage}</Typography>
        )}
      </Box>
    </Box>
  );
}

export default Search;
