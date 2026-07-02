import { useNavigate } from "react-router-dom";

export default function Dashboard() {
  const navigate = useNavigate();

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">Dashboard</h1>

      <div className="grid grid-cols-3 gap-4">
        <div className="bg-white p-4 shadow rounded">Total Requests: 10</div>
        <div className="bg-white p-4 shadow rounded">Pending: 3</div>
        <div className="bg-white p-4 shadow rounded">AI Runs: 7</div>
      </div>

      <button
        onClick={() => navigate("/evaluation/1")}
        className="mt-6 bg-blue-600 text-white px-4 py-2 rounded"
      >
        Run AI Evaluation
      </button>
    </div>
  );
}