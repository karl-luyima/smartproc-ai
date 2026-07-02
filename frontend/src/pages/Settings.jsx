export default function Settings() {
  return (
    <div className="ml-64 p-6">
      <h1 className="text-xl font-bold mb-4">Settings</h1>

      <div className="bg-white p-4 shadow rounded">
        <p>User Profile</p>
        <input className="border p-2 w-full mt-2" placeholder="Name" />

        <p className="mt-4">Theme</p>
        <select className="border p-2 w-full">
          <option>Light</option>
          <option>Dark</option>
        </select>
      </div>
    </div>
  );
}