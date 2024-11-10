import axios from 'axios';

const BASE_URL = process.env.REACT_APP_API_BASE_URL || 'http://localhost:5000';

export async function fetchSearchResults(query) {
  try {
    const response = await axios.get(`${BASE_URL}/search`, {
      params: {
        q: query,
      },
    });

    // list of objects in the required shape
    return response.data;

    // Test output
    // return [
    //   {
    //     title: 'hithere',
    //     text: 'mynameis',
    //     link: 'www.google.com'
    //   }
    // ];
  } catch (error) {
    console.error('Error fetching search results:', error);
    throw error;
  }
}
