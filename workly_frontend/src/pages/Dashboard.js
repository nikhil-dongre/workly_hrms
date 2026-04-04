import React from "react";
import { Link, Routes, Route } from "react-router-dom";

function Dashboard() {
  return (
    <div style={{ display: "flex" }}>
      
      {/* Sidebar */}
      <div style={{ width: "250px", background: "#f0f0f0", padding: "10px" }}>
        <h3>HRMS</h3>

        <p><b>Profile</b></p>
        <ul>
          <li><Link to="personal">Personal</Link></li>
          <li><Link to="contact">Contact</Link></li>
          <li><Link to="employment">Employment</Link></li>
        </ul>

        <p><b>Attendance</b></p>
        <ul>
          <li><Link to="punchin">Punch In</Link></li>
          <li><Link to="punchout">Punch Out</Link></li>
          <li><Link to="attendance">My Attendance</Link></li>
        </ul>

        <p><b>Leave</b></p>
        <ul>
          <li><Link to="applyleave">Apply Leave</Link></li>
          <li><Link to="myleaves">My Leaves</Link></li>
        </ul>
      </div>

      {/* Main Content */}
      <div style={{ marginLeft: "20px", padding: "10px" }}>
        
        <Routes>
          <Route path="/" element={<h2>Dashboard</h2>} />

          <Route path="personal" element={<h2>Personal Info Page</h2>} />
          <Route path="contact" element={<h2>Contact Info Page</h2>} />
          <Route path="employment" element={<h2>Employment Info Page</h2>} />

          <Route path="punchin" element={<h2>Punch In Page</h2>} />
          <Route path="punchout" element={<h2>Punch Out Page</h2>} />
          <Route path="attendance" element={<h2>My Attendance Page</h2>} />

          <Route path="applyleave" element={<h2>Apply Leave Page</h2>} />
          <Route path="myleaves" element={<h2>My Leaves Page</h2>} />
        </Routes>

      </div>

    </div>
  );
}

export default Dashboard;