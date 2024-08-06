import React, { useState, useMemo, useEffect } from 'react';
import { Tabs, Tab, Card, CardContent, Typography, TextField, Button, Box, CssBaseline, ThemeProvider, createTheme, LinearProgress } from '@mui/material';
import { ThemeProvider as Emotion10ThemeProvider } from '@emotion/react';
import { useTheme } from '@mui/system';
import { orangeDarkTheme, orangeLightTheme, basicTheme, darkTheme, lightTheme, customTheme, blueLightTheme, blueDarkTheme, greenLightTheme, greenDarkTheme, redLightTheme, redDarkTheme } from '../layout/themes';
import { GlobalStyles } from '../layout/GlobalStyle';
import { useNavigate } from 'react-router-dom';
import { toast } from 'react-toastify';
import useApi from '../hooks/APIHandler';

const Auth = () => {
  const [tab, setTab] = useState(0);
  const [themeMode, setThemeMode] = useState('basic');
  const navigate=useNavigate();
  const {callApi, error, loading} = useApi();
  useEffect(() => {
    const savedTheme = localStorage.getItem('theme') || 'basic';
    setThemeMode(savedTheme);
  }, []);

  let theme = useMemo(
    () => {
      switch(themeMode){
        case 'basic':
          return createTheme(basicTheme);
        case 'dark':
          return createTheme(darkTheme);
        case 'light':
          return createTheme(lightTheme);
        case 'custom':
          return createTheme(customTheme);
        case 'blue light':
          return createTheme(blueLightTheme);
        case 'blue dark':
          return createTheme(blueDarkTheme);
        case 'green light':
          return createTheme(greenLightTheme);
        case 'green dark':
          return createTheme(greenDarkTheme);
        case 'red light':
          return createTheme(redLightTheme);
        case 'red dark':
          return createTheme(redDarkTheme);
        case 'orange light':
          return createTheme(orangeLightTheme);
        case 'orange dark':
          return createTheme(orangeDarkTheme);
        default:
          return createTheme(lightTheme);
      }
    },
    [themeMode]
  );


  const goHome=() => {
    navigate('/ReactMUIDashboard/');
  }

  const handleChange = (event, newValue) => {
    setTab(newValue);
  };

  const doSignUp = async(e) => {
    e.preventDefault();
    let response = await callApi({
        url: 'auth/signup/',
        method: 'POST',
        body: {
            username: e.target.username.value,
            password: e.target.password.value,
            email: e.target.email.value,
            profile_pic: "https://dummyimage.com/600x400/000/fff"
        },
    })

    if(response?.data?.access){
        localStorage.setItem('token', response.data.access);
        toast.success("Signup successful");
        navigate('/');
    }else {
        toast.error("Signup failed");
    }

    console.log(response);
}

const doLogin = async(e) => {
    e.preventDefault();
    let response = await callApi({
        url: 'auth/login/',
        method: 'POST',
        body: {
            username: e.target.username.value,
            password: e.target.password.value
        },
    })

    if(response?.data?.access){
        localStorage.setItem('token', response.data.access);
        toast.success("Login successful");
        navigate('/');
    }else {
        toast.error("Invalid credentials");
    }

    console.log(response);
}

  return (
    <Emotion10ThemeProvider theme={theme}>
      <ThemeProvider theme={theme}>
        <CssBaseline />
        <GlobalStyles />
        <Box
          sx={{
            display: 'flex',
            justifyContent: 'center',
            alignItems: 'center',
            height: '100vh',
            backgroundColor: theme.palette.background.default
          }}
        >
          <Card sx={{ maxWidth: 400, width: '100%' }}>
            <CardContent>
              <Box sx={{ display: 'flex', justifyContent: 'center', mb: 2 }}>
                <img src={'https://picsum.photos/100'} alt="Logo" style={{ borderRadius: '50%' }} />
              </Box>
              <Typography variant="h5" align="center" gutterBottom>
                EzyMarket
              </Typography>
              <Tabs value={tab} onChange={handleChange} centered>
                <Tab label="Sign Up" />
                <Tab label="Sign In" />
              </Tabs>
              {tab === 0 && (
                <Box component="form" sx={{ mt: 2 }} onSubmit={doSignUp}>
                  <TextField
                    margin="normal"
                    required
                    fullWidth
                    label="Username"
                    name="username"
                    autoComplete="username"
                    autoFocus
                  />
                  <TextField
                    margin="normal"
                    required
                    fullWidth
                    label="Email"
                    name="email"
                    type="email"
                    autoComplete="email"
                  />
                  <TextField
                    margin="normal"
                    required
                    fullWidth
                    label="Password"
                    name="password"
                    type="password"
                    autoComplete="current-password"
                  />
                  {loading? <LinearProgress sx={{width: '100%'}} />:<Button
                    type="submit"
                    fullWidth
                    variant="contained"
                    color="primary"
                    sx={{ mt: 3, mb: 2 }}
                  >
                    Sign Up
                  </Button>}
                </Box>
              )}
              {tab === 1 && (
                <Box component="form" sx={{ mt: 2 }} onSubmit={doLogin}>
                  <TextField
                    margin="normal"
                    required
                    fullWidth
                    label="Username"
                    name="username"
                    autoComplete="username"
                    autoFocus
                  />
                  <TextField
                    margin="normal"
                    required
                    fullWidth
                    label="Password"
                    name="password"
                    type="password"
                    autoComplete="current-password"
                  />
                  {loading? <LinearProgress sx={{width: '100%'}} />:<Button
                    type="submit"
                    fullWidth
                    variant="contained"
                    color="primary"
                    sx={{ mt: 3, mb: 2 }}
                  >
                    Sign In
                  </Button>}
                </Box>
              )}
            </CardContent>
            <Box sx={{ textAlign: 'center', py: 2, borderTop: '1px solid', borderColor: theme.palette.divider }}>
              <Typography variant="body2" color="text.secondary">
                © 2024 EzyMarket. All rights reserved.
              </Typography>
            </Box>
          </Card>
        </Box>
      </ThemeProvider>
    </Emotion10ThemeProvider>
  );
};

export default Auth;