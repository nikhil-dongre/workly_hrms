import React, { useEffect, useState } from "react";

function Contact() {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    const token = localStorage.getItem("access_token");

    const response = await fetch("http://127.0.0.1:8000/api/employee/contact/", {
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
      <h2>Contact Info</h2>

      <p>phone: {data.phone}</p>
      <p>address: {data.address}</p>
      <p>emergency_contact: {data.emergency_contact}</p>
      <p>place_of_birth: {data.place_of_birth}</p>
    </div>
  );
}

export default Contact;