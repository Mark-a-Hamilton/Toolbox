#!/usr/bin/env python3
# ┌────────────────────────────────────────────────────────┐
# │ Version        : 2026.07.24-00                         │
# │ Author         : Mark Hamilton │ Co-Pilot AI assisted  │
# │ Script Purpose : Lightweight CORS-enabled HTTP server  │
# │ Package        : toolbox                               │
# └────────────────────────────────────────────────────────┘
#
# Usage:
#   server.py [--dry-run] [--verbose] [--log] [--hashmap]
#
# Description:
#   Runs a simple HTTP server on port 8080 with permissive CORS headers.
#   GET requests return a static greeting. POST requests log the received
#   body to data.html and return a confirmation message. Useful for testing
#   webhooks, client requests, or cross-origin behaviour.
#
# Output Files:
#   /var/log/server.py.log              (when --log is used)
#   .hashmap/server.py.hash             (when --hashmap is used)
#   .hashmap/server.py.timestamp        (when --hashmap is used)
#
# End Help

import argparse
import os
import sys
import hashlib
import datetime
from http.server import SimpleHTTPRequestHandler, HTTPServer

# ─── Metadata ─────────────────────────────────────────────
TOOL_NAME = "server.py"
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

# ─── Custom Handler ───────────────────────────────────────
class CustomRequestHandler(SimpleHTTPRequestHandler):

    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello, GET request!")

    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length).decode('utf-8')

        self.send_response(200)
        self.end_headers()

        with open("data.html", "a") as file:
            file.write(post_data + "\n")

        response = f"THM, POST request! Received data: {post_data}"
        self.wfile.write(response.encode("utf-8"))

# ─── Main Logic ───────────────────────────────────────────
def main_logic(args):
    log(f"Starting {TOOL_NAME} version {VERSION}", args.verbose)

    if args.dry_run:
        print("[DRY-RUN] HTTP server startup simulated.")
        return

    server_address = ("", 8080)
    httpd = HTTPServer(server_address, CustomRequestHandler)

    print("[+] Server running on http://localhost:8080/")
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
                
