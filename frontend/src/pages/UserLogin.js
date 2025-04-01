import { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

export default function UserLogin() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState(null);
  const navigate = useNavigate();

  const login = async () => {
    try {
      const response = await axios.post("http://localhost:8000/auth/login", {
        email,
        password,
      });
      localStorage.setItem("token", response.data.access_token);
      setError(null);
      navigate("/tasks");
    } catch {
      setError("❌ Login fallido.");
    }
  };

  return (
    <div className="p-8 max-w-md mx-auto">
      <h2 className="text-xl font-bold mb-4">Iniciar sesión</h2>
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
        className="w-full p-2 border rounded mb-4"
      />
      <button
        onClick={login}
        className="w-full bg-blue-600 text-white py-2 rounded hover:bg-blue-700"
      >
        Ingresar
      </button>
      {error && <p className="text-red-600 mt-4">{error}</p>}
    </div>
  );
}
