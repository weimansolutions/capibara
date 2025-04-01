import { useState } from 'react';
import axios from 'axios';

export default function UserTasks() {
  const [tasks, setTasks] = useState([]);
  const [userId, setUserId] = useState("");
  const [error, setError] = useState(null);

  const token = localStorage.getItem("token") || "";

  const fetchTasks = async () => {
    try {
      const response = await axios.get(`http://localhost:8000/tasks/usuario/${userId}`, {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });
      setTasks(response.data);
      setError(null);
    } catch {
      setError("No se pudieron obtener las tareas. Verificá el token o el ID.");
    }
  };

  return (
    <div className="p-8 max-w-2xl mx-auto">
      <h2 className="text-xl font-bold mb-4">Tareas del Usuario</h2>
      <input
        type="text"
        placeholder="ID del Usuario"
        value={userId}
        onChange={(e) => setUserId(e.target.value)}
        className="w-full p-2 border rounded mb-4"
      />
      <button
        onClick={fetchTasks}
        className="w-full bg-blue-600 text-white py-2 rounded hover:bg-blue-700"
      >
        Obtener Tareas
      </button>
      {error && <p className="text-red-600 mt-4">{error}</p>}
      <ul className="mt-4 space-y-2">
        {tasks.map((tarea) => (
          <li
            key={tarea.id}
            className="p-4 border rounded bg-white shadow flex justify-between items-center"
          >
            <span>{tarea.titulo}</span>
            <span className={`text-sm px-2 py-1 rounded ${tarea.estado === 'completada' ? 'bg-green-200 text-green-800' : 'bg-yellow-200 text-yellow-800'}`}>
              {tarea.estado}
            </span>
          </li>
        ))}
      </ul>
    </div>
  );
}
