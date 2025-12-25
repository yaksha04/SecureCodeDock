#!/bin/bash

echo " Creating reports directory..."
mkdir -p reports

echo " Running security scan with Bandit..."
bandit -r app.py -f txt -o reports/bandit_report.txt

echo " Installing Python dependencies..."
pip install -r requirements.txt > reports/deploy_log.txt 2>&1

echo " Building Docker image..."
docker build -t secure-python-app:latest . >> reports/deploy_log.txt 2>&1

echo " Removing old container (if exists)..."
docker rm -f secure_python_app >/dev/null 2>&1

echo " Deploying container..."
docker run -d --name secure_python_app -p 8080:8080 secure-python-app:latest >> reports/deploy_log.txt 2>&1

echo " Pipeline completed successfully."
echo " Check reports/ for Bandit scan and deployment logs."
