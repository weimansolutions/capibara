'use client';

import { useState } from 'react';
import { useRouter } from 'next/navigation';

export default function LoginForm() {
  const router = useRouter();
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');

  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault();
    setError('');

    const formData = new URLSearchParams();
    formData.append('grant_type', 'password');
    formData.append('username', username);
    formData.append('password', password);
    formData.append('scope', '');
    formData.append('client_id', 'string');
    formData.append('client_secret', 'string');

    try {
      const res = await fetch('http://34.204.120.187:8000/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
          Accept: 'application/json',
        },
        body: formData.toString(),
        credentials: 'include', 
      });

      if (!res.ok) {
        const err = await res.json();
        setError(err.detail || 'Usuario o contraseña incorrectos');
        return;
      }

      const data = await res.json();
      console.log('TOKEN:', data.access_token); // podés guardarlo en localStorage si querés

      router.push('/dashboard');
    } catch (err: any) {
      setError('Error de red o servidor no disponible');
    }
  };

  return (
    <form onSubmit={handleLogin} className="flex flex-col gap-4 p-6 border rounded w-full max-w-sm">
      <h2 className="text-xl font-bold">Iniciar sesión</h2>

      {error && <p className="text-red-500">{error}</p>}

      <input
        type="text"
        placeholder="Usuario"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
        className="border px-3 py-2 rounded"
        required
      />

      <input
        type="password"
        placeholder="Contraseña"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        className="border px-3 py-2 rounded"
        required
      />

      <button type="submit" className="bg-blue-500 text-white py-2 rounded hover:bg-blue-600">
        Entrar
      </button>
    </form>
  );
}
