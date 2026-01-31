import { useEffect, useState } from "react";
import { fetchAIInsights } from "../api";

export default function AIInsights({ data }) {
  const [loading, setLoading] = useState(false);
  const [analysis, setAnalysis] = useState("");

  useEffect(() => {
    if (!data) return;

    setLoading(true);
    fetchAIInsights(data)
      .then((res) => {
        if (res.status === "success") {
          setAnalysis(res.analysis);
        } else {
          setAnalysis("AI analysis unavailable");
        }
      })
      .catch(() => setAnalysis("AI analysis unavailable"))
      .finally(() => setLoading(false));
  }, [data]);

  return (
    <div className="card">
      <h3>🤖 AI Financial Insights</h3>

      {loading ? (
        <p>Analyzing financial data...</p>
      ) : (
        <pre style={{ whiteSpace: "pre-wrap", lineHeight: "1.6" }}>
          {analysis || "No insights generated"}
        </pre>
      )}
    </div>
  );
}
