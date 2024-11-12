import axios from 'axios';

const BASE_URL = process.env.REACT_APP_API_BASE_URL || 'http://localhost:5000';

export async function fetchSearchResults(query) {
  console.log('Trying to request from:', `${BASE_URL}/search`);
  
  try {
    const response = await axios.get(`${BASE_URL}/search`, {
      params: {
        q: query,
      },
    });
    
    console.log('Full API Response:', response); // Debugging line
    
    // list of objects in the required shape
    return response.data.results;
  } catch (error) {
    console.error('API Error while fetching search results:', error);
    throw error;
  }
}
