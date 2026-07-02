import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { getEvaluation } from "../services/api";

export default function Evaluation() {
  const { id } = useParams();
  const [data, setData] = useState(null);

  useEffect(() => {
    getEvaluation(id).then((res) => setData(res.data));
  }, [id]);

  if (!data) return <div className="ml-64 p-6">Loading AI...</div>;

  const result = data.decision;

  return (
    <div className="ml-64 p-6 space-y-6">
      <h1 className="text-2xl font-bold">AI Evaluation</h1>

      {/* WINNER CARD */}
      <div className="bg-white p-6 shadow rounded">
        <h2 className="text-xl font-bold">
          🏆 {result.best_vendor.vendor_name}
        </h2>
        <p>Score: {result.best_vendor.score}</p>
        <p>Confidence: {result.confidence}%</p>
      </div>

      {/* CHART (simple visual using HTML bars) */}
      <div className="bg-white p-6 shadow rounded">
        <h2 className="font-bold mb-3">Vendor Scores</h2>

        {result.scores.map((v, i) => (
          <div key={i} className="mb-2">
            <p>{v.vendor_name}</p>
            <div className="bg-gray-200 h-3 rounded">
              <div
                className="bg-blue-600 h-3 rounded"
                style={{ width: `${v.score}%` }}
              ></div>
            </div>
          </div>
        ))}
      </div>

      {/* REASONING */}
      <div className="bg-white p-6 shadow rounded">
        <h2 className="font-bold mb-2">AI Reasoning</h2>
        <ul className="list-disc ml-5">
          {result.reasoning.map((r, i) => (
            <li key={i}>{r}</li>
          ))}
        </ul>
      </div>

      {/* RISK */}
      <div className="bg-white p-6 shadow rounded">
        <h2 className="font-bold">Risk Summary</h2>
        {result.risk_summary.map((r, i) => (
          <p key={i}>⚠ {r.join(", ")}</p>
        ))}
      </div>
    </div>
  );
}