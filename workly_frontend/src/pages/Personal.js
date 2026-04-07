import React, { useEffect, useState } from "react";

function Personal() {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    const token = localStorage.getItem("access_token");

    const response = await fetch("http://127.0.0.1:8000/api/employee/personal/", {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });

    const result = await response.json();
    setData(result);
  };

  if (!data) return <p>Loading...</p>;

  return (
    <div>
      <h2>Personal Info</h2>

      <p>First Name: {data.first_name}</p>
      <p>Last Name: {data.last_name}</p>
      <p>Email: {data.email}</p>
      <p>Place of Birth: {data.place_of_birth}</p>
    </div>
  );
}

export default Personal;