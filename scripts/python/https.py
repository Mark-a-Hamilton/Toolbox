#!/usr/bin/env python3
# ┌────────────────────────────────────────────────────────┐
# │ Version        : 2026.07.24-00                         │
# │ Author         : Mark Hamilton │ Co-Pilot AI assisted  │
# │ Script Purpose : Launch a minimal HTTPS server         │
# │ Package        : toolbox                               │
# └────────────────────────────────────────────────────────┘
#
# Usage:
#   https.py [--dry-run] [--verbose] [--log] [--hashmap]
#
# Description:
#   Starts a simple HTTPS listener bound to 0.0.0.0:8002 using BaseHTTPRequestHandler.
#   The server socket is wrapped with TLS using cert.pem and key.pem, enabling secure
#   HTTPS communication. Intended for testing, local service exposure, or controlled
#   environments requiring a lightweight TLS-enabled endpoint.
#
# Output Files:
#   /var/log/https.py.log                 (when --log is used)
#   .hashmap/https.py.hash                (when --hashmap is used)
#   .hashmap/https.py.timestamp           (when --hashmap is used)
#
# End Help

import argparse
import os
import sys
import ssl
import hashlib
import datetime
from http.server import HTTPServer, BaseHTTPRequestHandler

# ─── Metadata ─────────────────────────────────────────────
TOOL_NAME = "https.py"
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

    if args.dry_run:
        print("[DRY-RUN] HTTPS server startup simulated.")
        return

    log("Initialising HTTPS server on 0.0.0.0:8002", args.verbose)

    httpd = HTTPServer(('0.0.0.0', 8002), BaseHTTPRequestHandler)

    log("Wrapping socket with TLS using cert.pem and key.pem", args.verbose)

    httpd.socket = ssl.wrap_socket(
        httpd.socket,
        keyfile="key.pem",
        certfile="cert.pem",
        server_side=True
    )

    print("[+] HTTPS server running on https://0.0.0.0:8002")
    httpd.serve_forever()

# ─── Main Entry Point ─────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(description=f"{TOOL_NAME} — toolbox Python tool")
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
                   
