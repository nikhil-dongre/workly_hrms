import React, { useState, useEffect } from "react";
import { Link, Routes, Route } from "react-router-dom";

function Attendancedata() {
  console.log("inside attendance page");
  const [message, setMessage] = useState("");
  const [status, setStatus] = useState("");
  const [totalHours, setTotalHours] = useState("");

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
    fetchTodayAttendance(); // 🔥 auto refresh
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
    fetchTodayAttendance(); // 🔥 auto refresh
  };
  const fetchTodayAttendance = async () => {
    try {
      const token = localStorage.getItem("access_token");

      const response = await fetch(
        "http://127.0.0.1:8000/api/attendance/today/",
        {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        },
      );

      const result = await response.json();

      if (response.ok) {
        setStatus(result.status);
        setTotalHours(result.data?.total_worked_hours || "00:00");
      } else {
        setMessage(result.error || "Failed to fetch");
      }
    } catch (error) {
      console.error(error);
      setMessage("Error fetching data");
    }
  };
  useEffect(() => {
    fetchTodayAttendance();
  }, []);
  return (
    <div style={{ padding: "10px" }}>
      <h2>Register Attendace</h2>

      <p>Status: {status}</p>
      <p>Total Hours: {totalHours}</p>

      <button onClick={handlePunchIn} disabled={status === "IN"}>
        Punch In
      </button>

      <br />
      <br />

      <button onClick={handlePunchOut} disabled={status === "OUT"}>
        Punch Out
      </button>

      {message && <p>{message}</p>}
    </div>
  );
}
export default Attendancedata;
