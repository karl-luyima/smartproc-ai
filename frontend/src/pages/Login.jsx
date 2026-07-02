import { useNavigate } from "react-router-dom";
import { login } from "../services/auth";

export default function Login() {
  const navigate = useNavigate();

  const handleLogin = () => {
    login("demo", "demo");
    navigate("/dashboard");
  };

  return (
    <div className="h-screen flex items-center justify-center">
      <button
        onClick={handleLogin}
        className="bg-blue-600 text-white px-6 py-2 rounded"
      >
        Login
      </button>
    </div>
  );
}