import { useState } from 'react';
import axios from 'axios';

export default function CreateEmpresa() {
  const [nombre, setNombre] = useState("");
  const [mensaje, setMensaje] = useState(null);

  const crearEmpresa = async () => {
    try {
      const response = await axios.post("http://localhost:8000/users/empresa", {
        nombre,
      });
      setMensaje(`✅ Empresa creada con ID: ${response.data.id}`);
    } catch {
      setMensaje("❌ Error al crear empresa.");
    }
  };

  return (
    <div className="p-8 max-w-md mx-auto">
      <h2 className="text-xl font-bold mb-4">Crear Empresa</h2>
      <input
        type="text"
        placeholder="Nombre de la empresa"
        value={nombre}
        onChange={(e) => setNombre(e.target.value)}
        className="w-full p-2 border rounded mb-4"
      />
      <button
        onClick={crearEmpresa}
        className="w-full bg-purple-600 text-white py-2 rounded hover:bg-purple-700"
      >
        Crear Empresa
      </button>
      {mensaje && <p className="mt-4 text-center">{mensaje}</p>}
    </div>
  );
}