// src/app/page.tsx
import Link from 'next/link';

export default function LandingPage() {
  return (
    <div className="min-h-screen bg-white dark:bg-gray-900 text-gray-900 dark:text-gray-100">
      <header className="px-6 py-4 shadow-md bg-gray-100 dark:bg-gray-800 flex justify-between items-center">
        <h1 className="text-xl font-bold">Capibara App</h1>
        <nav className="space-x-4">
          <Link href="/login" className="hover:underline">
            Iniciar sesión
          </Link>
          <Link href="#features" className="hover:underline">
            Características
          </Link>
          <Link href="#contact" className="hover:underline">
            Contacto
          </Link>
        </nav>
      </header>

      <main className="px-6 py-12 text-center">
        <h2 className="text-4xl font-bold mb-4">Bienvenido a Capibara App</h2>
        <p className="text-lg mb-6">Una plataforma simple para gestionar tus operaciones con eficiencia.</p>
        <Link href="/login" className="inline-block bg-blue-600 text-white px-6 py-3 rounded hover:bg-blue-700">
          Comenzar
        </Link>
      </main>

      <section id="features" className="px-6 py-12 bg-gray-50 dark:bg-gray-800">
        <h3 className="text-2xl font-semibold mb-6 text-center">Características</h3>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 text-left">
          <div className="p-4 border rounded shadow">
            <h4 className="font-bold">Gestión eficiente</h4>
            <p>Organizá tareas, usuarios y datos en una interfaz limpia.</p>
          </div>
          <div className="p-4 border rounded shadow">
            <h4 className="font-bold">Seguridad</h4>
            <p>Autenticación segura y estructura robusta para tus datos.</p>
          </div>
          <div className="p-4 border rounded shadow">
            <h4 className="font-bold">Adaptable</h4>
            <p>Diseñado para crecer con vos: ideal para SaaS o herramientas internas.</p>
          </div>
        </div>
      </section>

      <section id="contact" className="px-6 py-12">
        <h3 className="text-2xl font-semibold mb-6 text-center">Contacto</h3>
        <p className="text-center">¿Tenés dudas o querés colaborar? Escribinos a contacto@capibara.app</p>
      </section>

      <footer className="px-6 py-4 bg-gray-100 dark:bg-gray-800 text-center text-sm">
        © {new Date().getFullYear()} Capibara App. Todos los derechos reservados.
      </footer>
    </div>
  );
}
