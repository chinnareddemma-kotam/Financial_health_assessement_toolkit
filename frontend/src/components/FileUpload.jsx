import { useState } from "react";
import axios from "axios";
import * as XLSX from "xlsx";

// 🔗 Backend base URL (Render)
// In .env → VITE_API_URL=https://financial-health-assessement-toolkit-5xsl.onrender.com
const API_BASE =
  import.meta.env.VITE_API_URL ||
  "https://financial-health-assessement-toolkit-5xsl.onrender.com";

export default function FileUpload({ onResult }) {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);

  // Convert different file formats → CSV or text
  const parseFile = async (file) => {
    const ext = file.name.split(".").pop().toLowerCase();

    // CSV / TXT → send directly
    if (ext === "csv" || ext === "txt") return file;

    // XLSX → convert to CSV
    if (ext === "xlsx") {
      const buffer = await file.arrayBuffer();
      const workbook = XLSX.read(buffer);
      const sheet = workbook.Sheets[workbook.SheetNames[0]];
      const csv = XLSX.utils.sheet_to_csv(sheet);

      return new File([csv], "data.csv", { type: "text/csv" });
    }

    // PDF → send raw (backend decides)
    if (ext === "pdf") return file;

    // Other text-based formats
    const textBasedExts = [
      "json",
      "md",
      "log",
      "xml",
      "yaml",
      "yml",
      "ini",
      "cfg",
    ];

    if (textBasedExts.includes(ext)) {
      const text = await file.text();
      return new File([text], file.name, { type: "text/plain" });
    }

    alert("Unsupported file type");
    return null;
  };

  const handleUpload = async () => {
    if (!file) {
      alert("Please upload a file");
      return;
    }

    setLoading(true);

    try {
      const processedFile = await parseFile(file);
      if (!processedFile) return;

      const formData = new FormData();
      formData.append("file", processedFile);

      const response = await axios.post(
        `${API_BASE}/predict`,
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        }
      );

      onResult(response.data);
    } catch (error) {
      console.error("Upload error:", error.response || error);
      alert(
        error.response?.data?.detail ||
        "Upload failed. Check backend logs."
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ marginBottom: "20px" }}>
      <input
        type="file"
        accept=".csv,.txt,.xlsx,.pdf,.json,.md,.log,.xml,.yaml,.yml,.ini,.cfg"
        onChange={(e) => setFile(e.target.files[0])}
      />

      <button onClick={handleUpload} disabled={loading}>
        {loading ? "Uploading..." : "Upload"}
      </button>
    </div>
  );
}
