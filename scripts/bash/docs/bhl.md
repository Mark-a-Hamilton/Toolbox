# 📘 **bhl — BloodHound + Neo4j Launcher**

## 1. Introduction

`bhl` is a unified launcher for **Neo4j** and **BloodHound**, designed for controlled lab environments, Windows PrivEsc training, and AD attack‑path visualisation workflows inside the Toolbox ecosystem.

It automates:

- Neo4j startup  
- service readiness checks  
- browser launch (Chromium‑compatible)  
- BloodHound startup  
- diagnostic‑only mode  
- full traceability via hashmap artefacts  

This tool is ideal for:

- quickly spinning up AD graph analysis environments  
- validating Neo4j health  
- troubleshooting port conflicts  
- producing reproducible diagnostic logs  

---

## 2. Usage

```bash
bhl [--dry-run] [--verbose] [--log] [--hashmap]
    [--diagnose-only] [--no-browser]
```

The tool must be run as root:

```bash
sudo bhl
```

---

## 3. Features

### 🧠 Automated Neo4j Launch  
Starts Neo4j in console mode and waits for HTTP responsiveness on port **7474**.

### 🔍 Service Readiness Detection  
Uses HTTP status codes (`200`, `302`, `401`) to confirm Neo4j is ready.

### 🦊 BloodHound Startup  
Launches BloodHound once Neo4j is responsive.

### 🌐 Browser Auto‑Launch  
Detects `chromium` or `chromium-browser` and opens the Neo4j interface automatically.  
Can be disabled with `--no-browser`.

### 🩺 Diagnostic‑Only Mode  
Runs a full Neo4j diagnostic suite without launching anything:

- process check  
- version check  
- port conflict detection  
- config inspection  
- script SHA‑256 fingerprint  

### 🧪 Dry‑Run Mode  
Simulates execution without running commands — ideal for testing.

### 🗂️ Hashmap Traceability  
Generates SHA‑256 hash and timestamp files for reproducible debugging.

---

## 4. Flags

- **`--dry-run`** — simulate execution without running commands  
- **`--verbose`** — print detailed execution logs  
- **`--log`** — write results to `/var/log/bhl.log`  
- **`--hashmap`** — generate `.hashmap/bhl.hash` and `.hashmap/bhl.timestamp`  
- **`--diagnose-only`** — run diagnostics only; do not launch Neo4j or BloodHound  
- **`--no-browser`** — skip browser launch  

---

## 5. Output

### 📄 Log File  
`/var/log/bhl.log`  
Contains:

- Neo4j startup attempts  
- readiness checks  
- BloodHound launch status  
- browser detection  
- diagnostic output  
- execution metadata  

### 🧾 Hashmap Files  
Stored in `.hashmap/`:

- `bhl.hash` — SHA‑256 hash of the script  
- `bhl.timestamp` — execution timestamp  

These files support reproducible debugging and traceability across runs.

---

## 6. Educational Notes

This tool demonstrates how **service orchestration** can be automated cleanly using Bash:

- readiness loops  
- port conflict detection  
- browser detection  
- controlled background process launch  
- structured diagnostics  
- traceability artefacts  

It is intentionally transparent and ideal for teaching AD graph tooling workflows.

---

## 7. Closure

This tool and its documentation were co‑authored with AI assistance.  
For responsible use, authorship transparency, and ethical notes, see the Toolbox README.

🔙 Return to **Toolbox**

---
