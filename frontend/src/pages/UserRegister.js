import { useState } from 'react';
import axios from 'axios';

export default function UserRegister() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [empresaId, setEmpresaId] = useState("");
  const [mensaje, setMensaje] = useState(null);

  const crearUsuario = async () => {
    try {
      const response = await axios.post("http://localhost:8000/users", {
        email,
        password,
        empresa_id: parseInt(empresaId),
      });
      setMensaje(`✅ Usuario creado con ID: ${response.data.id}`);
    } catch {
      setMensaje("❌ Error al crear usuario.");
    }
  };

  return (
    <div className="p-8 max-w-md mx-auto">
      <h2 className="text-xl font-bold mb-4">Registrar Usuario</h2>
      <input
        type="email"
        placeholder="Correo"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        className="w-full p-2 border rounded mb-2"
      />
      <input
        type="password"
        placeholder="Contraseña"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        className="w-full p-2 border rounded mb-2"
      />
      <input
        type="number"
        placeholder="ID Empresa"
        value={empresaId}
        onChange={(e) => setEmpresaId(e.target.value)}
        className="w-full p-2 border rounded mb-4"
      />
      <button
        onClick={crearUsuario}
        className="w-full bg-green-600 text-white py-2 rounded hover:bg-green-700"
      >
        Crear Usuario
      </button>
      {mensaje && <p className="mt-4 text-center">{mensaje}</p>}
    </div>
  );
}