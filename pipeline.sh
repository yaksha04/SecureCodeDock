#!/bin/bash
mkdir -p reports
echo " Running security scan..."
python3 scanner/scan.py

echo "Installing dependencies..."
cd app
pip install -r requirements.txt > ../reports/deploy_log.txt 2>&1
cd ..

echo " Building Docker image..."
docker build -t secure-python-app:latest . >> reports/deploy_log.txt 2>&1

echo " Deploying container..."
docker run -d --name secure_python_app -p 8080:8080 secure-python-app:latest >> reports/deploy_log.txt 2>&1

echo " Done. Check reports/ for logs."

