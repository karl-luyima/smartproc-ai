export default function Vendors() {
  const vendors = [
    { name: "TechSupply Ltd", rating: 4.7 },
    { name: "Global Procurement Co", rating: 4.1 },
    { name: "QuickSource Traders", rating: 3.6 },
  ];

  return (
    <div className="ml-64 p-6">
      <h1 className="text-xl font-bold mb-4">Vendors</h1>

      <div className="grid grid-cols-3 gap-4">
        {vendors.map((v, i) => (
          <div key={i} className="bg-white p-4 shadow rounded">
            <h2 className="font-bold">{v.name}</h2>
            <p>Rating: {v.rating}</p>
          </div>
        ))}
      </div>
    </div>
  );
}