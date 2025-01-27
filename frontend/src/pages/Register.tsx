import React from "react";

const Register = () => {
  return (
    <div className="flex items-center justify-center min-h-screen bg-gray-100">
      <div className="w-full max-w-md p-6 bg-white rounded-2xl shadow-md">
        <h2 className="text-2xl font-bold text-center text-gray-800">Register</h2>
        <form className="mt-6 space-y-4">
          <div>
            <label
              htmlFor="ownerName"
              className="block text-sm font-medium text-gray-700"
            >
              Vehicle Owner Name
            </label>
            <input
              type="text"
              id="ownerName"
              name="ownerName"
              className="w-full px-4 py-2 mt-1 border rounded-lg shadow-sm focus:ring-blue-500 focus:border-blue-500 border-gray-300"
              placeholder="Enter owner's name"
            />
          </div>
          <div>
            <label
              htmlFor="vehicleRegNumber"
              className="block text-sm font-medium text-gray-700"
            >
              Vehicle Registration Number
            </label>
            <input
              type="text"
              id="vehicleRegNumber"
              name="vehicleRegNumber"
              className="w-full px-4 py-2 mt-1 border rounded-lg shadow-sm focus:ring-blue-500 focus:border-blue-500 border-gray-300"
              placeholder="Enter vehicle registration number"
            />
          </div>
          <div>
            <label
              htmlFor="password"
              className="block text-sm font-medium text-gray-700"
            >
              Set Password
            </label>
            <input
              type="password"
              id="password"
              name="password"
              className="w-full px-4 py-2 mt-1 border rounded-lg shadow-sm focus:ring-blue-500 focus:border-blue-500 border-gray-300"
              placeholder="Enter your password"
            />
          </div>
          <button
            type="submit"
            className="w-full px-4 py-2 text-white bg-blue-600 rounded-lg shadow-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2"
          >
            Register
          </button>
        </form>
      </div>
    </div>
  );
};

export default Register;
