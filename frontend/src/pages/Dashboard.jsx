import { useState } from "react";
import FileUpload from "../components/FileUpload";
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
  LineChart,
  Line,
  CartesianGrid,
} from "recharts";
import "./Dashboard.css";

export default function Dashboard() {
  const [result, setResult] = useState(null);

  return (
    <div className="dashboard">
      <h1 className="title">💼 SME Financial Health Dashboard</h1>
      <FileUpload onResult={setResult} />

      {result && (
        <>
          {/* KPI CARDS */}
          <div className="kpi-grid">
            <KpiCard
              title="Avg Health Score"
              value={result.summary.avg_health_score}
              gradient="blue"
            />
            <KpiCard
              title="Healthy SMEs"
              value={result.summary.healthy}
              gradient="green"
            />
            <KpiCard
              title="Moderate SMEs"
              value={result.summary.moderate}
              gradient="orange"
            />
            <KpiCard
              title="Risky SMEs"
              value={result.summary.risky}
              gradient="red"
            />
          </div>

          {/* CHARTS */}
          <div className="chart-grid">
            <div className="card">
              <h3>📊 Health Score vs Revenue</h3>
              <ResponsiveContainer width="100%" height={300}>
                <BarChart data={result.data}>
                  <CartesianGrid strokeDasharray="3 3" />
                  <XAxis dataKey="Revenue" />
                  <YAxis />
                  <Tooltip />
                  <Bar dataKey="Health_Score" fill="#4ade80" />
                  <Bar dataKey="Revenue" fill="#60a5fa" />
                </BarChart>
              </ResponsiveContainer>
            </div>

            <div className="card">
              <h3>📈 Revenue vs Health Score</h3>
              <ResponsiveContainer width="100%" height={300}>
                <LineChart data={result.data}>
                  <CartesianGrid strokeDasharray="3 3" />
                  <XAxis dataKey="Revenue" />
                  <YAxis />
                  <Tooltip />
                  <Line type="monotone" dataKey="Revenue" stroke="#60a5fa" />
                  <Line type="monotone" dataKey="Health_Score" stroke="#4ade80" />
                </LineChart>
              </ResponsiveContainer>
            </div>
          </div>

          {/* TABLE */}
          <div className="card">
            <h3>📋 SME Records</h3>
            <div className="table-wrapper">
              <table>
                <thead>
                  <tr>
                    {Object.keys(result.data[0]).map((key) => (
                      <th key={key}>{key}</th>
                    ))}
                  </tr>
                </thead>
                <tbody>
                  {result.data.map((row, i) => (
                    <tr key={i}>
                      {Object.values(row).map((val, j) => (
                        <td key={j}>{val}</td>
                      ))}
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>
          {/* AI INSIGHTS */}
          <div className="card ai-insights">
            <h3>🤖 AI Financial Insights</h3>
            <pre style={{ whiteSpace: "pre-wrap", lineHeight: "1.6" }}>
              {result.ai_insights}
            </pre>
          </div>
        </>
      )}
    </div>
  );
}

/* KPI Component */
function KpiCard({ title, value, gradient }) {
  return (
    <div className={`kpi-card ${gradient}`}>
      <p>{title}</p>
      <h2>{value}</h2>
    </div>
  );
}

