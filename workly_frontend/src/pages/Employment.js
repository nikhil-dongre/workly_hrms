import React, { useEffect, useState } from "react";

function Employment() {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetchEmployee();
  }, []);

  const fetchEmployee = async () => {
    try {
        const token = localStorage.getItem("access_token");
        console.log("TOKEN:", token);

        if (!token) {
        alert("No token found. Please login again.");
        return;
        }

        const response = await fetch("http://127.0.0.1:8000/api/employee/me/", {
        method: "GET",
        headers: {
            "Authorization": `Bearer ${token}`,
        },
        });

        console.log("STATUS:", response.status);

        // 👇 Handle non-JSON response safely
        const contentType = response.headers.get("content-type");

        if (!response.ok) {
        const text = await response.text();
        console.error("ERROR RESPONSE:", text);
        return;
        }

        if (contentType && contentType.includes("application/json")) {
        const result = await response.json();
        console.log("DATA:", result);
        setData(result);
        } else {
        const text = await response.text();
        console.error("NOT JSON RESPONSE:", text);
        }

    } catch (error) {
        console.error("Error:", error);
    }
    };
  if (!data) return <p>Loading...</p>;

  return (
    <div>
      <h2>Employment Details</h2>

      <p>Employee Code: {data.emp_code}</p>
      <p>Name: {data.user_name}</p>
      <p>Email: {data.email}</p>
      <p>Department: {data.department}</p>
      <p>Designation: {data.designation}</p>
      <p>Joining Date: {data.joining_date}</p>
      <p>Phone: {data.phone}</p>
    </div>
  );
}

export default Employment;