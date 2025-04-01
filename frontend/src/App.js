import { BrowserRouter as Router, Routes, Route, Navigate, useNavigate } from 'react-router-dom';
import Navbar from './components/Navbar';
import Footer from './components/Footer';
import HomePage from './pages/HomePage';
import UserRegister from './pages/UserRegister';
import UserLogin from './pages/UserLogin';
import CreateEmpresa from './pages/CreateEmpresa';
import UserTasks from './pages/UserTasks';

function PrivateRoute({ children }) {
  const token = localStorage.getItem("token");
  return token ? children : <Navigate to="/login" />;
}

function App() {
  return (
    <Router>
      <div className="flex flex-col min-h-screen">
        <Navbar />
        <main className="flex-grow">
          <Routes>
            <Route path="/" element={<HomePage />} />
            <Route path="/register" element={<UserRegister />} />
            <Route path="/login" element={<UserLogin />} />
            <Route path="/empresa" element={<CreateEmpresa />} />
            <Route
              path="/tasks"
              element={
                <PrivateRoute>
                  <UserTasks />
                </PrivateRoute>
              }
            />
          </Routes>
        </main>
        <Footer />
      </div>
    </Router>
  );
}

export default App;