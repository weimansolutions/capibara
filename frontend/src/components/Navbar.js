import { Link, useNavigate } from 'react-router-dom';
import { useEffect, useState } from 'react';

export default function Navbar() {
  const navigate = useNavigate();
  const [email, setEmail] = useState("");
  const token = localStorage.getItem("token");
  const isLoggedIn = !!token;

  useEffect(() => {
    const payload = token?.split('.')[1];
    if (payload) {
      const decoded = JSON.parse(atob(payload));
      setEmail(decoded.sub || "");
    }
  }, [token]);

  const logout = () => {
    localStorage.removeItem("token");
    navigate("/login");
  };

  return (
    <nav className="bg-blue-600 text-white p-4 shadow">
      <div className="container mx-auto flex justify-between items-center">
        <Link to="/" className="text-xl font-bold">Mi App</Link>
        <div className="space-x-4 flex items-center">
          <Link to="/" className="hover:underline">Inicio</Link>
          <Link to="/empresa" className="hover:underline">Crear Empresa</Link>
          <Link to="/register" className="hover:underline">Registrar</Link>
          {!isLoggedIn ? (
            <Link to="/login" className="hover:underline">Login</Link>
          ) : (
            <>
              <span className="text-sm text-white/80">{email}</span>
              <button onClick={logout} className="hover:underline">Logout</button>
            </>
          )}
        </div>
      </div>
    </nav>
  );
}
