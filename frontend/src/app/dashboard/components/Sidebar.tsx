import Link from 'next/link';

export default function Sidebar() {
  return (
    <aside className="w-64 bg-white dark:bg-gray-800 border-r p-4 hidden md:block">
      <nav className="flex flex-col gap-2">
        <Link href="/dashboard" className="hover:bg-gray-200 dark:hover:bg-gray-700 rounded px-3 py-2">
          Inicio
        </Link>
        <Link href="/dashboard/ejemplo" className="hover:bg-gray-200 dark:hover:bg-gray-700 rounded px-3 py-2">
          Página de Ejemplo
        </Link>
      </nav>
    </aside>
  );
}
