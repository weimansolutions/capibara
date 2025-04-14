export default function PaginaEjemplo() {
    return (
      <div>
        <h2 className="text-xl font-bold mb-4">Tabla de Usuarios</h2>
        <table className="min-w-full bg-white dark:bg-gray-700 rounded shadow overflow-hidden">
          <thead>
            <tr className="text-left bg-gray-100 dark:bg-gray-600">
              <th className="p-3">ID</th>
              <th className="p-3">Nombre</th>
              <th className="p-3">Rol</th>
            </tr>
          </thead>
          <tbody>
            <tr className="border-t border-gray-200 dark:border-gray-600">
              <td className="p-3">1</td>
              <td className="p-3">Juan</td>
              <td className="p-3">Admin</td>
            </tr>
            <tr className="border-t border-gray-200 dark:border-gray-600">
              <td className="p-3">2</td>
              <td className="p-3">María</td>
              <td className="p-3">Usuario</td>
            </tr>
          </tbody>
        </table>
      </div>
    );
  }
  