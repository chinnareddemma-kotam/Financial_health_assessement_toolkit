import React from "react";
import ReactDOM from "react-dom/client";
import Dashboard from "./pages/Dashboard";

const App = () => {
  return (
    <>
      {/* ================= HERO SECTION ================= */}
      <section style={styles.hero}>
        <h1 style={styles.heroTitle}>
          SME Financial Health Assessment
        </h1>

        <p style={styles.heroSubtitle}>
          An AI-powered platform designed to help Small and Medium Enterprises
          evaluate their financial health, risk level, and credit readiness
          using data-driven insights.
        </p>

        <div style={styles.heroBadges}>
          <span>📊 Rule-Based Scoring</span>
          <span>🤖 Machine Learning Insights</span>
          <span>🏦 Bank-Ready Evaluation</span>
        </div>

        {/* EXISTING BUTTON */}
        <a href="#about" style={styles.ctaBtn}>
          Explore Platform ↓
        </a>

        {/* 🔥 NEW UPLOAD BUTTON (ADDED) */}
        <div style={{ marginTop: "20px" }}>
          <button
            onClick={() =>
              document
                .getElementById("upload-section")
                ?.scrollIntoView({ behavior: "smooth" })
            }
            style={{
              padding: "14px 32px",
              background: "#ffffff",
              color: "#1f3c88",
              fontWeight: "600",
              borderRadius: "30px",
              border: "none",
              cursor: "pointer",
            }}
          >
            Upload Financial Data ⬆️
          </button>
        </div>
      </section>

      {/* ================= ABOUT SECTION ================= */}
      <section id="about" style={styles.section}>
        <h2 style={styles.sectionTitle}>What is this platform?</h2>
        <p style={styles.sectionText}>
          The SME Financial Health Assessment platform helps businesses and
          financial institutions analyze financial statements and operational
          data to determine overall business stability, risk exposure, and
          loan eligibility.
        </p>

        <p style={styles.sectionText}>
          By combining rule-based scoring with machine learning models, the
          system provides reliable and explainable financial insights that
          assist banks, NBFCs, and SMEs in smarter decision-making.
        </p>
      </section>

      {/* ================= HOW IT WORKS ================= */}
      <section style={styles.sectionAlt}>
        <h2 style={styles.sectionTitle}>How it works</h2>

        <div style={styles.steps}>
          <div style={styles.stepCard}>
            <h3>📁 Upload Data</h3>
            <p>
              Upload SME financial data in CSV, XLSX, and PDF format including revenue,
              expenses, assets, liabilities, and cash flow.
            </p>
          </div>

          <div style={styles.stepCard}>
            <h3>⚙️ Smart Analysis</h3>
            <p>
              Backend processes the data using financial rules and ML models
              to generate health scores.
            </p>
          </div>

          <div style={styles.stepCard}>
            <h3>📈 Insights & Score</h3>
            <p>
              View health score, risk category, KPIs, and AI-generated
              recommendations.
            </p>
          </div>
        </div>
      </section>

      {/* ================= WHY IT MATTERS ================= */}
      <section style={styles.section}>
        <h2 style={styles.sectionTitle}>Why this matters</h2>
        <ul style={styles.list}>
          <li> Helps SMEs identify strengths & weaknesses</li>
          <li> Enables faster, fair loan assessment</li>
          <li> Reduces human bias using ML scoring</li>
          <li> Improves transparency in credit evaluation</li>
        </ul>
      </section>

      {/* ================= DASHBOARD ================= */}
      <section id="upload-section" style={styles.dashboard}>
        <Dashboard />
      </section>
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

/* ================= STYLES ================= */

const styles = {
  hero: {
    minHeight: "90vh",
    padding: "90px 20px",
    background: "linear-gradient(135deg, #1f3c88, #2851a3)",
    color: "#ffffff",
    textAlign: "center",
  },
  heroTitle: {
    fontSize: "3rem",
    fontWeight: "700",
    marginBottom: "20px",
  },
  heroSubtitle: {
    fontSize: "1.2rem",
    maxWidth: "850px",
    margin: "0 auto 30px",
    opacity: 0.95,
  },
  heroBadges: {
    display: "flex",
    justifyContent: "center",
    gap: "20px",
    flexWrap: "wrap",
    marginBottom: "35px",
    fontSize: "1rem",
  },
  ctaBtn: {
    display: "inline-block",
    padding: "14px 30px",
    background: "#ffffff",
    color: "#1f3c88",
    fontWeight: "600",
    borderRadius: "30px",
    textDecoration: "none",
  },
  section: {
    padding: "70px 20px",
    background: "#ffffff",
    textAlign: "center",
  },
  sectionAlt: {
    padding: "70px 20px",
    background: "#f3f6fb",
    textAlign: "center",
  },
  sectionTitle: {
    fontSize: "2.2rem",
    marginBottom: "25px",
  },
  sectionText: {
    maxWidth: "900px",
    margin: "0 auto 15px",
    fontSize: "1rem",
    lineHeight: "1.7",
  },
  steps: {
    display: "flex",
    gap: "25px",
    flexWrap: "wrap",
    justifyContent: "center",
    marginTop: "40px",
  },
  stepCard: {
    background: "#ffffff",
    padding: "25px",
    borderRadius: "12px",
    width: "280px",
    boxShadow: "0 8px 20px rgba(0,0,0,0.08)",
  },
  list: {
    maxWidth: "700px",
    margin: "0 auto",
    textAlign: "left",
    fontSize: "1.05rem",
    lineHeight: "1.8",
  },
  dashboard: {
    padding: "40px 20px",
    background: "#ededee",
  },
};
