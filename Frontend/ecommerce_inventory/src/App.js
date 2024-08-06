import './App.css';
import Home from './pages/Home';
import Layout from './layout/layout'
import { createBrowserRouter, RouterProvider } from 'react-router-dom';
import 'react-toastify/dist/ReactToastify.css';
import ProtectedRoute from './utils/ProtectedRoute';
import { ToastContainer } from 'react-toastify';
import Auth from './pages/Auth';
import store from './redux/store/store';
import { useDispatch, useSelector } from 'react-redux';
import { Provider } from 'react-redux';
import { fetchSidebar } from './redux/reducer/sidebardata';
import { useEffect, useState } from 'react';
import DynamicForm from './pages/DynamicForm'
import './style/style.css'
import ManageCategories from './pages/category/ManageCategories';


// const sidebarItems = [
//   {name: 'Home', link: '/home', icon: 'home'},
//   {name: 'Products', link: '/products', icon: 'products'},
//   {name: 'Categories', icon: 'categories', children: [
//     {name: 'All Categories', link: '/categories'}, {name: 'Add Category', link: '/categories/add'}
//   ]},
//   {name: 'Orders', link: '/orders', icon: 'orders'},
//   {name: 'Users', link: '/users', icon: 'users'},
//   {name: 'Settings', link: '/settings', icon: 'settings'},
// ]

function App() {
  const {status, error, items} = useSelector((state) => state.sidebardata);
  const dispatch = useDispatch();

  useEffect(() => {
    if (status == 'idle') {
      dispatch(fetchSidebar())
    }
  }, [status, dispatch])
  
  const router = createBrowserRouter([
    {path: "/auth", element: <Auth />},
    {
      path: "/", 
      element: <Layout sidebarList = {items} />,
      children: [
        {path:"/", element: <ProtectedRoute element={<Home />}/>},
        {path:"/form/:formName", element: <ProtectedRoute element={<DynamicForm />}/>},
        {path:"/manage/category", element: <ProtectedRoute element={<ManageCategories />}/>},
      ]
    },
  ]);

  return (
    <>
      <RouterProvider router={router} />
      <ToastContainer position='bottom-right' theme='colored' autoClose={3000} hideProgressBar={false} style={{marginBottom: '30px'}}/>
    </>
  );
}

export default App;
