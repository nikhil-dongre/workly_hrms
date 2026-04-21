import React, { useState } from "react";
import { Link, Routes, Route } from "react-router-dom";

function Attendancedata() {
  console.log("inside attendance page");
  const [message, setMessage] = useState("");

  const handlePunchIn = async () => {
    try {
      const token = localStorage.getItem("access_token");

      if (!token) {
        setMessage("Please login again");
        return;
      }

      const response = await fetch(
        "http://127.0.0.1:8000/api/attendance/punch_in/",
        {
          method: "POST",
          headers: {
            Authorization: `Bearer ${token}`,
          },
        },
      );

      const result = await response.json();

      if (response.ok) {
        setMessage(result.message);
      } else {
        setMessage(result.error || "Punch In failed");
      }
    } catch (error) {
      console.error(error);
      setMessage("Something went wrong");
    }
  };

  const handlePunchOut = async () => {
    try {
      const token = localStorage.getItem("access_token");
      if (!token) {
        setMessage("Please login first");
        return;
      }
      const response = await fetch(
        "http://127.0.0.1:8000/api/attendance/punch_out/",
        {
          method: "POST",
          headers: {
            Authorization: `Bearer ${token}`,
          },
        },
      );
      const result = await response.json();

      if (response.ok) {
        setMessage(result.message);
      } else {
        setMessage(result.error || "Punch In failed");
      }
    } catch (error) {
      console.error(error);
      setMessage("Something went wrong");
    }
  };
  return (
    <div style={{ padding: "10px" }}>
      <h2>Attendance Register</h2>

      <button onClick={handlePunchIn}>Punch In</button>
      <button onClick={handlePunchOut}>Punch Out</button>

      <br />
      <br />

      {message && <p>{message}</p>}
    </div>
  );
}
export default Attendancedata;
