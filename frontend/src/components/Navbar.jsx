export default function Navbar() {
  return (
    <div className="ml-64 h-14 bg-white shadow flex items-center justify-between px-6">
      <h2 className="font-semibold">Procurement System</h2>

      <div className="flex gap-4 items-center">
        <span>🔔</span>
        <span className="w-8 h-8 bg-gray-300 rounded-full"></span>
      </div>
    </div>
  );
}