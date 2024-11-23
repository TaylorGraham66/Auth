import React, { useState, useEffect } from 'react';
import axios from 'axios';

const App = () => {
    const [message, setMessage] = useState('');

    useEffect(() => {
        axios.get('http://127.0.0.1:5000/api/greet', { params: { name: 'React User' } })
            .then(response => setMessage(response.data.message))
            .catch(error => console.error('Error fetching data:', error));
    }, []);

    return (
        <div>
            <h1>Python + React</h1>
            <p>{message}</p>
        </div>
    );
};

export default App;
