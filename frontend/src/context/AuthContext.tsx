'use client';

import { createContext, useContext, useEffect, useState } from 'react';

interface AuthContextType {
  token: string | null;
  user: any | null; // podés tipar esto si sabés el contenido
  login: (newToken: string, userData?: any) => void;
  logout: () => void;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export function AuthProvider({ children }: { children: React.ReactNode }) {
  const [token, setToken] = useState<string | null>(null);
  const [user, setUser] = useState<any | null>(null);


  useEffect(() => {
    // Leer el token de las cookies si no hay en localStorage
    const storedToken = localStorage.getItem('token');
    const cookieToken = getCookie('token');

    if (storedToken) {
      setToken(storedToken);
    } else if (cookieToken) {
      setToken(cookieToken);
      localStorage.setItem('token', cookieToken); // opcional
    }
  }, []);

  const login = (newToken: string, userData?: any) => {
    localStorage.setItem('token', newToken);
    document.cookie = `token=${newToken}; path=/`;
    setToken(newToken);
    if (userData) setUser(userData);
  };
  

  const logout = () => {
    localStorage.removeItem('token');
    document.cookie = 'token=; path=/; max-age=0';
    setToken(null);
    setUser(null);
  };
  

  return (
    <AuthContext.Provider value={{ token, user, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
}

// 🔍 Utilidad para leer una cookie del navegador
function getCookie(name: string): string | null {
  const match = document.cookie.match(new RegExp('(^| )' + name + '=([^;]+)'));
  return match ? match[2] : null;
}

export function useAuth() {
  const context = useContext(AuthContext);
  if (!context) throw new Error('useAuth debe estar dentro de un AuthProvider');
  return context;
}
