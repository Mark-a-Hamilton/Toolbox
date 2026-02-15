# 🩺 diag

`diag` is a modular diagnostics and system‑health tool within the Toolbox suite.  
It performs uptime, memory, disk, service, and optional network diagnostics, with support for dry‑run simulation, logging, and hash‑based traceability.

---

## 🎯 Purpose

`diag` provides a fast, operator‑grade snapshot of system health by:

- Reporting uptime, memory, and disk usage  
- Checking service status and recent kernel messages  
- Optionally including network diagnostics  
- Supporting dry‑run mode for safe simulation  
- Logging results to `/var/log/diag.log`  
- Generating SHA‑256 hashes for audit trails via `.hashmap/`

This tool is designed for DFIR operators, system maintainers, and anyone needing a quick, reliable health overview.

---

## 🧪 Usage

### Basic Diagnostics
```bash
diag
```

### With Elevated Privileges
```bash
sudo diag
```

### Dry‑Run Mode
```bash
diag --dry-run
```
Simulates diagnostics without executing commands.

### Logging Mode
```bash
diag --log
```
Writes results to:
```
/var/log/diag.log
```

### Hash‑Based Audit Mode
```bash
diag --hashmap
```
Creates:
```
.hashmap/diag.hash
.hashmap/diag.timestamp
```

### Network Diagnostics
```bash
diag --network
```
Adds interface, routing, socket, and resolver checks.

---

## 🧩 Embedded Features

| Feature         | Description                                                  |
|----------------|--------------------------------------------------------------|
| Metadata Block | Standardised versioning (`2026.02.13‑01`) for traceability   |
| Flag Parsing   | Supports `--dry-run`, `--log`, `--hashmap`, `--network`      |
| Logging        | Writes timestamped diagnostics to `/var/log/diag.log`        |
| Hashmap        | SHA‑256 hashing + timestamp for audit trails                 |
| Help Block     | Auto‑displayed via `diag --help`                             |

---

## 🔧 Diagnostics Performed

| Check                        | Description                                      |
|------------------------------|--------------------------------------------------|
| `uptime`                     | System uptime                                    |
| `df -h`                      | Disk usage summary                               |
| `free -m`                    | Memory usage summary                             |
| `top -b -n 1 | head -20`     | CPU + process snapshot                           |
| `systemctl --failed`         | Failed service detection                         |
| `dmesg | tail -20`           | Recent kernel messages                           |
| **Network Mode (`--network`)** | Adds: `ip a`, `ip r`, `ss -tuln`, resolver info |

---

## 📁 Output Files

| File Path                   | When Created                | Purpose                          |
|-----------------------------|-----------------------------|----------------------------------|
| `/var/log/diag.log`         | `--log`                     | Timestamped diagnostic log       |
| `.hashmap/diag.hash`        | `--hashmap`                 | SHA‑256 hash of the script       |
| `.hashmap/diag.timestamp`   | `--hashmap`                 | Timestamp of hash generation     |

All output locations are explicitly shown during execution.

---

## 🤖 AI Integration

`diag` was refined using AI‑assisted development to ensure:

- consistent metadata  
- predictable flag behaviour  
- clean operator‑grade output  
- alignment with the Toolbox architecture  

The tool remains fully human‑auditable and transparent.

---

## 🧭 Contributor Guidance

- Follow the Toolbox versioning model: `YYYY.MM.DD‑BUILD`
- Keep diagnostics modular and readable
- Avoid hardcoded paths outside `/var/log/` and `.hashmap/`
- Validate metadata and formatting using:
  ```bash
  tool-box
  tool-box diag
  ```
- Document behavioural quirks directly in this file

---

## 🤖 AI & Ethics Disclosure  

This tool was co‑authored with AI assistance.  
For details on ethical integration and responsible authorship, see:  
ethics_AI.md [(github.com in Bing)](https://www.bing.com/search?q="https%3A%2F%2Fgithub.com%2FMark-a-Hamilton%2FMark-a-Hamilton.github.io%2Fblob%2Fmain%2Fethics_AI.md")

🔙 Return to [Toolbox](https://github.com/Mark-a-Hamilton/Toolbox)
