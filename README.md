# SecureCodeDock 🔐🐳  
**A Lightweight DevSecOps Pipeline with Security Scanning, Dockerization, and CLI Monitoring**

SecureCodeDock is a DevSecOps-focused automation project that demonstrates how security can be integrated early into the CI/CD lifecycle using static code analysis, containerization, and terminal-based observability.

## 🚀 Features

### 🔍 Static Security Scanning (Shift-Left Security)
- Uses **Bandit** to perform static analysis on Python source code
- Detects common security issues such as:
  - Insecure function usage
  - Hardcoded secrets
  - Unsafe imports
- Generates a detailed scan report in the `reports/` directory

### 🐳 Dockerized Application
- Builds a Docker image for the Python application
- Ensures environment consistency across systems
- Runs the application inside a container

### 📊 Terminal-Based Dashboard (CLI UI)
- Python-based terminal dashboard (`ui.py`)
- Displays:
  - Security scan results
  - Deployment logs
  - Pipeline execution status
- No browser UI — optimized for CI/CD environments

### ⚙️ Automated Pipeline Script
- Single command execution using `pipeline.sh`
- Orchestrates:
  1. Security scan
  2. Dependency installation
  3. Docker image build
  4. Container deployment


## 🧱 Project Structure

SecureCodeDock/
├── app.py # Sample Python application
├── scan.py # Bandit security scanning script
├── ui.py # Terminal-based dashboard
├── pipeline.sh # Main pipeline automation script
├── Dockerfile # Docker image definition
├── requirements.txt # Python dependencies
├── reports/ # Scan reports and deployment logs
├── venv/ # Python virtual environment
└── README.md


## 🛠️ Prerequisites

- Python 3.10+
- Docker
- Git
- Linux / WSL / macOS


## ⚙️ Setup & Execution

### 1️⃣ Clone the Repository

git clone https://github.com/yaksha04/SecureCodeDock.git
cd SecureCodeDock

2️⃣ Create & Activate Virtual Environment
python3 -m venv venv
source venv/bin/activate

3️⃣ Install Python Dependencies
pip install -r requirements.txt

4️⃣ Make Pipeline Executable
chmod +x pipeline.sh

5️⃣ Run the DevSecOps Pipeline
./pipeline.sh


This will:

Run Bandit security scan

Generate reports in reports/

Build Docker image

Deploy container

6️⃣ View Security Reports
cat reports/bandit_report.txt

7️⃣ Launch Terminal Dashboard (UI)
python3 ui.py

📌 Notes

This project focuses on static analysis, not runtime security

Security scan does not fail the pipeline by default (can be extended)

Designed as a learning-grade DevSecOps pipeline


🔮 Possible Enhancements

Add Trivy for container image scanning

Fail pipeline on high-severity vulnerabilities

Integrate GitHub Actions CI

Export reports to cloud storage

Add Kubernetes deployment


🎯 Why This Project?

Demonstrates DevSecOps fundamentals

Shows security-first mindset

Uses industry-relevant tools

Ideal for DevOps / DevSecOps internship interviews


👤 Author

Yaksha
DevOps & DevSecOps Enthusiast



