#!/usr/bin/env python3
# ┌────────────────────────────────────────────────────────┐
# │ Version        : 2026.07.24-00                         │
# │ Author         : Mark Hamilton │ Co-Pilot AI assisted  │
# │ Script Purpose : Generate db vulnerability reports     │
# │ Package        : toolbox                               │
# └────────────────────────────────────────────────────────┘
#
# Usage:
#   db-report.py --report <management|technical> [--dry-run] [--verbose] [--log] [--hashmap]
#
# Description:
#   Produces HTML-based management or technical reports summarising database
#   security findings, including detected vulnerabilities, extracted credentials,
#   severity ratings, and remediation priorities. Designed to be used after
#   running db-tool.py or similar analysis modules.
#
# Output Files:
#   /var/log/db-report.py.log            (when --log is used)
#   .hashmap/db-report.py.hash           (when --hashmap is used)
#   .hashmap/db-report.py.timestamp      (when --hashmap is used)
#
# End Help

import argparse
import os
import sys
import hashlib
import datetime

# ─── Metadata ─────────────────────────────────────────────
TOOL_NAME = "db-report.py"
VERSION = "2026.07.24-00"

LOGFILE = f"/var/log/{TOOL_NAME}.log"
HASHDIR = ".hashmap"
HASHFILE = f"{HASHDIR}/{TOOL_NAME}.hash"
TIMESTAMP = f"{HASHDIR}/{TOOL_NAME}.timestamp"

# ─── Helpers ──────────────────────────────────────────────
def log(msg, verbose):
    if verbose:
        print(f"[LOG] {msg}")

def run_step(cmd, dry_run, verbose):
    if dry_run:
        print(f"[DRY-RUN] Would execute: {cmd}")
    else:
        log(f"Executing: {cmd}", verbose)
        os.system(cmd)

def write_log(dry_run, verbose, logging, hashmap):
    if logging and not dry_run:
        os.makedirs(os.path.dirname(LOGFILE), exist_ok=True)
        with open(LOGFILE, "a") as lf:
            lf.write("=== " + TOOL_NAME + " ===\n")
            lf.write(str(datetime.datetime.now()) + "\n")
            lf.write(f"Version: {VERSION}\n")
            lf.write(f"Flags: DRY_RUN={dry_run} VERBOSE={verbose} LOGGING={logging} HASHMAP={hashmap}\n")
            lf.write("====================\n")

def write_hashmap():
    os.makedirs(HASHDIR, exist_ok=True)
    with open(TIMESTAMP, "w") as tf:
        tf.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    with open(HASHFILE, "w") as hf:
        with open(sys.argv[0], "rb") as sf:
            hf.write(hashlib.sha256(sf.read()).hexdigest())

# ─── Report Generators ────────────────────────────────────
def generate_management_report(vulnerabilities, extracted_credentials):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"db_tool_management_{timestamp}.html"

    html_content = f"""<!DOCTYPE html>
<html>
<head>
    <title>Database Security Analysis - Management Report</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 20px; }}
        h1 {{ color: #003366; }}
        .section {{ margin-bottom: 20px; padding: 10px; border: 1px solid #ddd; background: #f8f8f8; }}
    </style>
</head>
<body>
    <h1>Database Security Analysis - Management Report</h1>
    <p><strong>Report Generated:</strong> {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>

    <div class='section'>
        <h2>Summary</h2>
        <p>This report provides a high-level overview of database security vulnerabilities.</p>
    </div>

    <div class='section'>
        <h2>Detected Vulnerabilities</h2>
        <ul>
            {"".join(f"<li>{v}</li>" for v in vulnerabilities)}
        </ul>
    </div>

    <div class='section'>
        <h2>Extracted Credentials</h2>
        <ul>
            {"".join(f"<li>{u}: {p}</li>" for u, p in extracted_credentials.items())}
        </ul>
    </div>

    <div class='section'>
        <h2>Recommendations</h2>
        <ul>
            <li>Ensure proper input validation to prevent SQL/NoSQL injection.</li>
            <li>Implement database security best practices to protect user credentials.</li>
            <li>Enhance monitoring tools to detect malicious activities.</li>
        </ul>
    </div>
</body>
</html>"""

    with open(filename, "w") as file:
        file.write(html_content)
    print(f"[+] Management report saved as: {filename}")

def generate_technical_report(vulnerabilities, extracted_credentials, severity_ratings, remediation_priority):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"db_tool_technical_{timestamp}.html"

    html_content = f"""<!DOCTYPE html>
<html>
<head>
    <title>Database Security Analysis - Technical Report</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 20px; }}
        h1 {{ color: #003366; }}
        .section {{ margin-bottom: 20px; padding: 10px; border: 1px solid #ddd; background: #f8f8f8; }}
    </style>
</head>
<body>
    <h1>Database Security Analysis - Technical Report</h1>
    <p><strong>Report Generated:</strong> {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>

    <div class='section'>
        <h2>Summary</h2>
        <p>This report provides a technical breakdown of database vulnerabilities and mitigation strategies.</p>
    </div>

    <div class='section'>
        <h2>Detected Vulnerabilities & Severity Ratings</h2>
        <ul>
            {"".join(f"<li>{v} - Severity: {severity_ratings[v]}</li>" for v in vulnerabilities)}
        </ul>
    </div>

    <div class='section'>
        <h2>Extracted Credentials</h2>
        <ul>
            {"".join(f"<li>{u}: {p}</li>" for u, p in extracted_credentials.items())}
        </ul>
    </div>

    <div class='section'>
        <h2>Recommended Security Fixes</h2>
        <ul>
            {"".join(f"<li>{fix}</li>" for fix in remediation_priority)}
        </ul>
    </div>

    <div class='section'>
        <h2>Mitigation Strategies</h2>
        <ul>
            <li>Use parameterized queries to eliminate SQL injection risks.</li>
            <li>Enforce proper access control mechanisms for database security.</li>
            <li>Implement monitoring and anomaly detection for suspicious queries.</li>
            <li>Sanitize user input to prevent exploitation.</li>
        </ul>
    </div>
</body>
</html>"""

    with open(filename, "w") as file:
        file.write(html_content)
    print(f"[+] Technical report saved as: {filename}")

# ─── Main Logic ───────────────────────────────────────────
def main_logic(args):
    log(f"Starting {TOOL_NAME} version {VERSION}", args.verbose)

    # Example findings (placeholder for db-tool.py output)
    vulnerabilities = ["SQL Injection Detected", "NoSQL Injection Possible"]
    extracted_credentials = {"admin": "password123", "user1": "securePass"}
    severity_ratings = {"SQL Injection Detected": "High", "NoSQL Injection Possible": "Medium"}
    remediation_priority = [
        "Fix SQLi vulnerabilities immediately.",
        "Enhance input validation.",
        "Implement logging and monitoring."
    ]

    if args.dry_run:
        print("[DRY-RUN] Report generation simulated.")
        return

    if args.report == "management":
        generate_management_report(vulnerabilities, extracted_credentials)
    elif args.report == "technical":
        generate_technical_report(vulnerabilities, extracted_credentials, severity_ratings, remediation_priority)

# ─── Main Entry Point ─────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(description=f"{TOOL_NAME} — toolbox Python tool")
    parser.add_argument("--report", choices=["management", "technical"], required=True,
                        help="Select report type to generate.")
    parser.add_argument("--dry-run", action="store_true", help="Simulate actions without executing")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose logging")
    parser.add_argument("--log", action="store_true", help="Write execution details to log file")
    parser.add_argument("--hashmap", action="store_true", help="Generate traceability files")
    args = parser.parse_args()

    main_logic(args)

    if args.log:
        write_log(args.dry_run, args.verbose, args.log, args.hashmap)

    if args.hashmap:
        write_hashmap()

if __name__ == "__main__":
    main()
  
