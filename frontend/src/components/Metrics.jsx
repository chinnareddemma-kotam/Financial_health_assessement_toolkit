export default function Metrics({ summary }) {
  if (!summary) return null;

  return (
    <div className="metrics">
      <div>⭐ Avg Score: {summary.avg_health_score}</div>
      <div>🟢 Healthy: {summary.healthy}</div>
      <div>🟡 Moderate: {summary.moderate}</div>
      <div>🔴 Risky: {summary.risky}</div>
    </div>
  );
}
