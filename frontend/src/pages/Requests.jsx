import { useNavigate } from "react-router-dom";

export default function Requests() {
  const navigate = useNavigate();

  return (
    <div className="p-6">
      <h1 className="text-xl font-bold mb-4">Procurement Requests</h1>

      {[1, 2, 3].map((id) => (
        <div key={id} className="bg-white p-3 shadow mb-2 flex justify-between">
          <span>Request #{id}</span>

          <button
            onClick={() => navigate(`/evaluation/${id}`)}
            className="bg-green-600 text-white px-3 py-1 rounded"
          >
            Evaluate
          </button>
        </div>
      ))}
    </div>
  );
}