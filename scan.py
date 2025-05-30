import os
import subprocess

# Ensure the 'reports' directory exists
os.makedirs("../reports", exist_ok=True)

# Path to scan
scan_target = "../app"

# Output file path
output_path = "../reports/scan_report.txt"

# Run bandit scan
try:
    print(f" Running Bandit scan on {scan_target}...")
    result = subprocess.run(
        ["bandit", "-r", scan_target],
        capture_output=True,
        text=True
    )

    # Save scan results
    with open(output_path, "w") as report_file:
        report_file.write(" Bandit Security Scan Report\n")
        report_file.write("---------------------------------\n")
        report_file.write(result.stdout)

    print(f" Bandit scan completed. Report saved to: {output_path}")

except Exception as e:
    print(f" Error during Bandit scan: {e}")



