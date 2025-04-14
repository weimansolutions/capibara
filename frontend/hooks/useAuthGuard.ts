// hooks/useAuthGuard.ts
'use client';

import { useEffect, useState } from 'react';
import { useRouter } from 'next/navigation';
import { jwtDecode } from 'jwt-decode';
import { useAuth } from '@/context/AuthContext';

interface JwtPayload {
  exp: number;
  sub: string;
  [key: string]: any; // Para permitir payloads personalizados
}

export function useAuthGuard(redirectIfInvalid = '/login') {
  const router = useRouter();
  const [authorized, setAuthorized] = useState<boolean | null>(null);
  const { login } = useAuth();

  useEffect(() => {
    const tokenCookie = document.cookie
      .split('; ')
      .find((row) => row.startsWith('token='));

    if (!tokenCookie) {
      router.replace(redirectIfInvalid);
      return;
    }

    const token = tokenCookie.split('=')[1];

    try {
      const decoded = jwtDecode<JwtPayload>(token);
      const now = Math.floor(Date.now() / 1000);

      if (decoded.exp > now) {
        login(token, decoded); // Guardamos el token y el usuario
        setAuthorized(true);
      } else {
        router.replace(redirectIfInvalid);
      }
    } catch (err) {
      router.replace(redirectIfInvalid);
    }
  }, [router, redirectIfInvalid, login]);

  return authorized;
}