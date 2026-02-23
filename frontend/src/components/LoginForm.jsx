# Epic Title: Responsive Design for Mobile using React

import React, { useState } from 'react';
import axios from 'axios';

const LoginForm = () => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [mfaToken, setMfaToken] = useState('');
    const [mfaPrompt, setMfaPrompt] = useState(false);
    const [error, setError] = useState('');

    const handleLogin = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post('/api/login', { email, password });
            if (response.data.token) {
                setMfaPrompt(true);
            }
        } catch (err) {
            setError('Invalid credentials');
        }
    };

    const handleMfaValidation = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post('/api/mfa/validate', { account_id: email, token: mfaToken });
            if (response.data.success) {
                alert('Login successful');
            } else {
                setError('Invalid MFA code');
            }
        } catch (err) {
            setError('Failed to validate MFA code');
        }
    };

    if (mfaPrompt) {
        return (
            <form onSubmit={handleMfaValidation}>
                <div>
                    <label>MFA Code</label>
                    <input
                        type="text"
                        value={mfaToken}
                        onChange={(e) => setMfaToken(e.target.value)}
                    />
                </div>
                <button type="submit">Submit</button>
                {error && <p>{error}</p>}
            </form>
        );
    }

    return (
        <form onSubmit={handleLogin}>
            <div>
                <label>Email</label>
                <input
                    type="email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                />
            </div>
            <div>
                <label>Password</label>
                <input
                    type="password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                />
            </div>
            <button type="submit">Login</button>
            {error && <p>{error}</p>}
        </form>
    );
};

export default LoginForm;