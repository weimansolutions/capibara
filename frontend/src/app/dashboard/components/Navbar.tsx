'use client';

import { useState, useEffect } from 'react';
import { useRouter } from 'next/navigation';

export default function Navbar() {
  const [darkMode, setDarkMode] = useState(false);
  const router = useRouter();

  useEffect(() => {
    document.documentElement.classList.toggle('dark', darkMode);
  }, [darkMode]);

  const handleLogout = async () => {
    localStorage.removeItem('token');
    document.cookie = 'token=; path=/; max-age=0';  
    await fetch('http://34.204.120.187:8000/logout', {
      method: 'POST',
      credentials: 'include',
    });
    router.push('/login');
  };

  return (
    <nav className="flex items-center justify-between px-6 py-3 border-b bg-white dark:bg-gray-800 shadow">
      <h1 className="text-lg font-bold">Mi Aplicación</h1>
      <div className="flex items-center gap-4">
        <button
          onClick={() => setDarkMode(!darkMode)}
          className="px-3 py-1 rounded bg-gray-200 dark:bg-gray-700"
        >
          {darkMode ? '☀️ Claro' : '🌙 Oscuro'}
        </button>
        <button
          onClick={handleLogout}
          className="px-3 py-1 rounded bg-red-500 text-white hover:bg-red-600"
        >
          Cerrar sesión
        </button>
      </div>
    </nav>
  );
}
