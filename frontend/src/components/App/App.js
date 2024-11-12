import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { Box, Container, createTheme, CssBaseline, ThemeProvider } from '@mui/material';
import Search from '../Search/Search'
import Landing from '../Landing/Landing'


const theme = createTheme({
  palette: {
    mode: 'dark',
    primary: {
      main: '#2ba143',
    },
    // mode: 'light',
    // primary: {
    //   main: '#15622f',
    // },
    secondary: {
      main: '#c74141',
    },
    info: {
      main: '#9021f3',
    },
  },
});


function App() {
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Router>
        <Background />
        <Container maxWidth="lg" sx={{ position: 'relative', zIndex: 1 }}>
          <Routes>
            <Route path="/" element={<Landing />} />
            <Route path="/search" element={<Search />} />
          </Routes>
        </Container>
      </Router>
    </ThemeProvider>
  );
}


function Background() {
  return (
    <Box
      sx={{
        position: 'fixed',
        top: 0,
        left: 0,
        width: '100%',
        height: '100%',
        backgroundImage: 'url("/wallpaper.png")',
        backgroundSize: 'cover',
        backgroundRepeat: 'no-repeat',
        backgroundPosition: 'center',
        zIndex: -1,
      }}
    />
  );
}


export default App;
