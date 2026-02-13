# 🩺 tool-diag

`tool-diag` is a modular diagnostics and system health tool for Kali Linux. It performs checks on uptime, memory, disk usage, and service status, with optional dry-run, logging, and hash-based traceability.

---

## 📦 Purpose

This tool helps assess system health and operational readiness by:

- Reporting uptime, memory, and disk usage
- Checking service status (e.g. Neo4j, BloodHound)
- Logging diagnostics with timestamps
- Generating SHA-256 hashes for audit trails

---

## 🚀 Usage

### Basic Diagnostics
```bash
tool-diag
```
Runs all diagnostic checks directly.

### Dry-Run Mode
```bash
tool-diag --dry-run
```
Simulates diagnostics without executing commands.

### With Logging
```bash
tool-diag --log
```
Appends diagnostic results to `/var/log/tool-diag.log`.

### With Hash-Based Audit
```bash
tool-diag --hashmap
```
Generates a SHA-256 hash of the script and logs the timestamp to `.hashmap/`.

---

## ⚙️ Parameters

| Flag         | Description                                      |
|--------------|--------------------------------------------------|
| `--dry-run`  | Simulates diagnostics without executing          |
| `--log`      | Logs results to `/var/log/tool-diag.log`         |
| `--hashmap`  | Stores script hash and timestamp in `.hashmap/`  |
| `--network`  | Includes network diagnostics (e.g. ping, route)  |
| `--help`     | Displays usage instructions                      |

---

## 🔧 Diagnostics Performed

| Check              | Description                                |
|--------------------|--------------------------------------------|
| `uptime`           | System uptime                              |
| `free -h`          | Memory usage summary                       |
| `df -h`            | Disk usage summary                         |
| `systemctl status` | Service health checks                      |
| `ping`, `ip route` | Optional network diagnostics               |

---

## 📁 Output

- Console summary of system health
- Optional log file with timestamped diagnostics
- Optional `.hashmap/` entry for audit traceability

---

## 🤖 AI & Ethics Disclosure  

This tool was co-authored with AI assistance. For full details on ethical integration, traceability, and responsible authorship, see [ethics_AI.md]([https://mark-a-hamilton.github.io/main/ethics_AI.md](https://github.com/Mark-a-Hamilton/Mark-a-Hamilton.github.io/blob/main/ethics_AI.md)).  
🔙 [Return to Kali-toolbox](https://github.com/Mark-a-Hamilton/kali-toolbox)
