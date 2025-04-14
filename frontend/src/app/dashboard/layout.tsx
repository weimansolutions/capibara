'use client';

import { useEffect, useState } from 'react';
import { useRouter } from 'next/navigation';
import { jwtDecode } from 'jwt-decode';
import Navbar from './components/Navbar';
import Sidebar from './components/Sidebar';

interface JwtPayload {
  exp: number;
  sub: string;
}

export default function DashboardLayout({ children }: { children: React.ReactNode }) {
  const router = useRouter();
  const [isAuthorized, setIsAuthorized] = useState<boolean | null>(null);

  useEffect(() => {
    const tokenCookie = document.cookie
      .split('; ')
      .find((row) => row.startsWith('token='));

    if (!tokenCookie) {
      router.replace('/login');
      return;
    }

    const token = tokenCookie.split('=')[1];

    try {
      const decoded = jwtDecode<JwtPayload>(token);


      const now = Math.floor(Date.now() / 1000);
      if (decoded.exp < now) {
        console.warn('Token expirado');
        router.replace('/login');
        return;
      }

      // Token válido
      setIsAuthorized(true);
    } catch (err) {
      console.error('Token inválido:', err);
      router.replace('/login');
    }
  }, [router]);

  if (isAuthorized === null) return null;

  return (
    <div className="flex min-h-screen bg-gray-100 dark:bg-gray-900 text-gray-900 dark:text-gray-100">
      <Sidebar />
      <div className="flex-1 flex flex-col">
        <Navbar />
        <main className="p-6 flex-1 overflow-y-auto">{children}</main>
      </div>
    </div>
  );
}
