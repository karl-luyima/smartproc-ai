import { Link } from "react-router-dom";

export default function Sidebar() {
  return (
    <div className="h-screen w-64 bg-gray-900 text-white p-4 fixed">
      <h1 className="text-xl font-bold mb-6">SmartProc AI</h1>

      <nav className="flex flex-col gap-3">
        <Link to="/dashboard">Dashboard</Link>
        <Link to="/requests">Requests</Link>
        <Link to="/vendors">Vendors</Link>
        <Link to="/quotes">Quotes</Link>
        <Link to="/reports">Reports</Link>
        <Link to="/settings">Settings</Link>
        <Link to="/assistant">AI Assistant</Link>
      </nav>
    </div>
  );
}