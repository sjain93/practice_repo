import axios from 'axios';
//instance of axios client with a few defaulted properties, customized just towards making request to spceific url with specfic headers
export default axios.create({
    baseURL: 'https://api.unsplash.com',
    headers: {
        Authorization: 'Client-ID 8ac1bb04b0f7d3287c5ea86ca28a95fab465e192b4d0cc0960977d273e0fb4d2'
    }
});