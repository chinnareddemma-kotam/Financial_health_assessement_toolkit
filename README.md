## 💼 SME Financial Health Assessment Platform

An AI-powered fintech platform that analyzes SME financial data to evaluate creditworthiness, risk, and business health, combining rule-based intelligence, machine learning, and optional LLM insights.

## 🚀 Problem Statement

Small and Medium Enterprises (SMEs) often lack access to affordable, data-driven financial advisory tools. Banks and NBFCs need explainable, scalable, and fast methods to assess SME financial health beyond manual underwriting.

## 🎯 Solution Overview

This platform enables users to:

Upload SME financial data via CSV

Automatically compute key financial ratios

Assign Health Scores & Risk Categories

Generate actionable financial insights

Persist results for historical analysis

Optionally enhance insights using Generative AI (Gemini)

## 🔗 Project Links & Deployments
# 🔙 Backend (FastAPI)

# Repository
https://github.com/chinna-reddemma/sme-financial-health-backend

# API Base URL (Deployed)
https://financial-health-assessement-toolkit-5xsl.onrender.com

# Swagger API Docs
https://financial-health-assessement-toolkit-5xsl.onrender.com/docs

# Deployment Platform: Render

Service Name: financial-health-assessment-toolkit

## 🎨 Frontend (React Dashboard)

# Repository
https://github.com/chinna-reddemma/sme-financial-health-frontend

# Live Application
https://financial-health-toolkit-app.vercel.app/

# Deployment Platform: Vercel

# Project Name: financial-health-toolkit-app

# 🧠 Key Features
✅ Financial Scoring Engine

Cost Ratio

Profit Margin

Net Profitability

Rule-based Health Score (0–100)

✅ SME Classification

Healthy

Moderate

Risky

✅ AI / Rule-Based Insights

Dynamic recommendations based on portfolio health

Deterministic fallback logic (no hallucinations)

Optional Gemini LLM integration for advanced insights

✅ Data Persistence

Stores uploaded records with timestamps

Supports future analytics & trend analysis

✅ Frontend Dashboard

KPI cards (Average Health, Risk Breakdown)

Charts: Revenue vs Health Score

Tabular SME records

AI Insights panel

## 🏗️ System Architecture

React Frontend
     |
     
     | REST API
     v
     
FastAPI Backend

     |

     ├── Rule-Based Engine
     
     ├── ML Model (Health Confidence)
     
     ├── Optional Gemini LLM
     
     └── Database (SQLite / PostgreSQL-ready)


## 🛠️ Tech Stack
Frontend

React

Chart.js / Recharts

Axios

Backend

FastAPI

Pandas

Scikit-learn

Joblib

AI (Optional)

Google Gemini API

Database

SQLite (default)

PostgreSQL compatible

## 📂 Project Structure
financial-health/
├── backend/
│   ├── main.py
│   ├── models/
│   ├── llm/
│   ├── database/
│   └── financial_health_model.pkl
├── frontend/
│   ├── src/
│   ├── components/
│   └── pages/
├── sample_data/
│   └── sme_financials.csv
├── README.md
└── requirements.txt

## 📊 Input CSV, XLSX, PDF Format or any other text format

Required columns

Revenue
COGS
OperatingExpenses
NetProfit


Optional (auto-calculated if missing)

Cost_Ratio
Profit_Margin

## ⚙️ How It Works

User uploads SME financial CSV

Backend validates & preprocesses data

Financial ratios are computed

Health score & status assigned

Portfolio summary generated

Insights produced (Rule-Based or AI)

Results stored & returned to frontend

## 🤖 AI Insights Logic
# Rule-Based (Default)

Ensures explainability and consistency

# Adjusts recommendations based on:

Average Health Score

Risk distribution

Gemini AI (Optional)

Enable via environment variable:

GEMINI_API_KEY=your_key_here

## 🔐 Security & Reliability

No financial data is shared externally unless AI is enabled

Environment-based API key management

Deterministic fallback ensures reliability

## 📈 Future Enhancements

Role-based login (Admin / Analyst)

SME-level personalized recommendations

Credit eligibility prediction

PDF financial reports

Bank/NBFC product matching

GST & compliance checks

## 🏆 Use Cases

Banks & NBFCs

MSME Loan Underwriting

Fintech Risk Platforms

Financial Advisors

Hackathons & Demos

## 👨‍💻 Author

## Chinna Reddemma
AI/ML Enthusiast

Built with ❤️ as a real-world fintech solution, not just a demo.
