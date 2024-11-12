import axios from 'axios';

let BASE_URL = '';  // Initialize an empty URL

// Fetch the base URL dynamically from the Flask API
async function fetchBaseUrl() {
  try {
    const response = await axios.get('/api/base_url');
    BASE_URL = response.data.base_url;  // Set the base URL dynamically
    console.log('Fetched Base URL:', BASE_URL);
  } catch (error) {
    console.error('Error fetching base URL:', error);
    BASE_URL = 'http://localhost:5000';  // Fallback to localhost if error
  }
}

// Use the dynamic BASE_URL for your search requests
export async function fetchSearchResults(query) {
  // Ensure the base URL is set before making a request
  if (!BASE_URL) {
    await fetchBaseUrl();  // Fetch the URL if not already set
  }

  try {
    console.log('Trying to request from:', `${BASE_URL}/search`);
    
    const response = await axios.get(`${BASE_URL}/search`, {
      params: {
        q: query,
      },
    });
    
    console.log('Full API Response:', response); // Debugging line
    
    return response.data.results;  // List of objects in the required shape
  } catch (error) {
    console.error('API Error while fetching search results:', error);
    throw error;
  }
}
