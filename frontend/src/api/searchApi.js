import axios from 'axios';

async function fetchBaseUrl() {
  try {
    const response = await axios.get('/api/base_url');
    return response.data.base_url;
  } catch (error) {
    console.error('Error fetching base URL:', error);
    return 'http://localhost:5000'; // Fallback to localhost
  }
}

export async function fetchSearchResults(query) {
  const BASE_URL = await fetchBaseUrl();
  console.log('Trying to request from:', `${BASE_URL}/search`);

  try {
    const response = await axios.get(`${BASE_URL}/search`, {
      params: {
        q: query,
      },
    });
    console.log('Full API Response:', response);
    return response.data.results;
  } catch (error) {
    console.error('API Error while fetching search results:', error);
    throw error;
  }
}
