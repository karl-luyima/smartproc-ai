export default function Reports() {
  return (
    <div className="ml-64 p-6">
      <h1 className="text-xl font-bold mb-4">Reports</h1>

      <div className="bg-white p-4 shadow rounded">
        <h2 className="font-bold">Procurement Report</h2>
        <p>Download AI-generated procurement analysis reports.</p>

        <button className="mt-3 bg-blue-600 text-white px-4 py-2 rounded">
          Download PDF
        </button>
      </div>
    </div>
  );
}