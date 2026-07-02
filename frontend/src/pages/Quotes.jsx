export default function Quotes() {
  const quotes = [
    { vendor: "TechSupply", price: 720, days: 11 },
    { vendor: "Global Procurement", price: 900, days: 14 },
  ];

  return (
    <div className="ml-64 p-6">
      <h1 className="text-xl font-bold mb-4">Vendor Quotes</h1>

      <table className="w-full bg-white shadow">
        <thead>
          <tr>
            <th>Vendor</th>
            <th>Price</th>
            <th>Delivery</th>
          </tr>
        </thead>

        <tbody>
          {quotes.map((q, i) => (
            <tr key={i}>
              <td className="p-2">{q.vendor}</td>
              <td>{q.price}</td>
              <td>{q.days} days</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}