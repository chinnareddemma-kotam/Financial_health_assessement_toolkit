const BASE = import.meta.env.VITE_API_URL
  || "https://financial-health-assessement-toolkit-5xsl.onrender.com";

// Upload CSV
export async function uploadCSV(file) {
  const formData = new FormData();
  formData.append("file", file);

  const res = await fetch(`${BASE}/predict`, {
    method: "POST",
    body: formData,
  });

  if (!res.ok) {
    throw new Error("Upload failed");
  }

  return res.json();
}

// ✅ AI Insights
export async function fetchAIInsights(data) {
  const res = await fetch(`${BASE}/ai-insights`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ data }),
  });

  if (!res.ok) {
    throw new Error("AI Insights failed");
  }

  return res.json();
}

// ✅ AI Explanation
export async function getAIExplanation(payload) {
  const res = await fetch(`${BASE}/ai/explain`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });

  if (!res.ok) {
    throw new Error("AI Explanation failed");
  }

  return res.json();
}
