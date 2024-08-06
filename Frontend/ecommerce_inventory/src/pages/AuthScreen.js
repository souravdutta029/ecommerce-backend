import React, { useEffect, useState } from 'react';
import { Box, Tabs, Tab, Card, TextField, Button, Typography, LinearProgress } from '@mui/material';
import useApi from '../hooks/APIHandler';
import { toast } from 'react-toastify';
import { useNavigate } from 'react-router-dom';



const AuthScreen = () => {
    const [tabIndex, setTabIndex] = useState(0);
    const navigate = useNavigate();
    const handleChange = (event, newIndex) => {
      setTabIndex(newIndex);
    };

    useEffect(() => {
        if(localStorage.getItem('token')) {
            navigate('/home');
        }
    }, [])
  
    
    return (
      <Box
        sx={{
          height: '100vh',
          display: 'flex',
          justifyContent: 'center',
          alignItems: 'center',
          backgroundColor: '#f0f0f0'
        }}
      >
        <Card sx={{ width: 400, p: 4, borderRadius: 2, boxShadow: 3 }}>
          <Tabs
            value={tabIndex}
            onChange={handleChange}
            variant="fullWidth"
            sx={{ mb: 2 }}
          >
            <Tab label="Sign Up" />
            <Tab label="Login" />
          </Tabs>
          {tabIndex === 0 && <SignUpForm/>}
          {tabIndex === 1 && <LoginForm/>}
        </Card>
      </Box>
    );
  };

const LoginForm = () => {
    const navigate = useNavigate();
    const {callApi, error, loading} = useApi();
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
            navigate('/home');
        }else {
            toast.error("Invalid credentials");
        }

        console.log(response);
    }
    
    return (
        <Box>
            <form onSubmit={doLogin}>
                <Typography variant="h6" gutterBottom>Login</Typography>
                <TextField
                label="Username"
                name="username"
                variant="outlined"
                fullWidth
                margin="normal"
                required
                />
                <TextField
                label="Password"
                name="password"
                variant="outlined"
                type="password"
                fullWidth
                margin="normal"
                required
                />
                {loading?<LinearProgress style={{width: '100%'}}/>:
                <Button type="submit" variant="contained" color="primary" fullWidth sx={{ mt: 2 }}>
                Login
                </Button>}
            </form>
        </Box>
    )
}

const SignUpForm = () => {
    const navigate = useNavigate();
    const {callApi, error, loading} = useApi();
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
            navigate('/home');
        }else {
            toast.error("Signup failed");
        }

        console.log(response);
    }

    return (
        <Box>
            <form onSubmit={doSignUp}>
                <Typography variant="h6" gutterBottom>Sign Up</Typography>
                <TextField
                label="Username"
                name='username'
                variant="outlined"
                fullWidth
                margin="normal"
                required
                />
                <TextField
                label="Email"
                name = 'email'
                variant="outlined"
                type="email"
                fullWidth
                margin="normal"
                required
                />
                <TextField
                label="Password"
                name ='password'
                variant="outlined"
                type="password"
                fullWidth
                margin="normal"
                required
                />
                {loading?<LinearProgress style={{width: '100%'}}/>:
                <Button type="submit" variant="contained" color="primary" fullWidth sx={{ mt: 2 }}>
                Sign Up
                </Button>}
            </form>
        </Box>
    )
}

export default AuthScreen;
