# 📘 **update — System Update & Locate DB Refresh Tool**

## 1. Introduction

`update` is a Toolbox module that performs a **complete system update** using APT, followed by a refresh of the system’s locate database. It is designed for authorised administrative use and provides a clean, reproducible workflow for maintaining system health.

It performs:

- full APT update + upgrade sequence  
- dependency repair via `--fix-broken`  
- autoremove + cache clean  
- locate database refresh (`updatedb`)  
- optional logging  
- optional hash‑based traceability  
- dry‑run simulation mode  

This tool is ideal for:

- daily maintenance  
- lab machine upkeep  
- PrivEsc training environments  
- reproducible update workflows  

---

## 2. Usage

```bash
sudo update [--dry-run] [--log] [--hashmap]
```

### Examples

```bash
sudo update --dry-run
sudo update --log
sudo update --hashmap
```

---

## 3. Features

### 🔄 Full APT Update Workflow  
Runs a complete update sequence:

- `apt update`  
- `apt --fix-broken install`  
- `apt full-upgrade`  
- `apt autoremove -y`  
- `apt clean`  

Ensures the system is fully upgraded and free of obsolete packages.

### 📚 Locate Database Refresh  
Runs `updatedb --verbose` and verifies freshness via:

```
stat -c '%y %n' /var/lib/plocate/plocate.db
```

Ensures accurate file indexing for `locate`.

### 🧪 Dry‑Run Mode  
Simulates all update steps without executing them — ideal for testing or CI pipelines.

### 📝 Logging  
Writes update steps and locate refresh output to:

```
/var/log/update.log
```

### 🗂️ Hashmap Traceability  
Generates:

- `.hashmap/update.hash` — SHA‑256 fingerprint of the script  
- `.hashmap/update.timestamp` — execution timestamp  

Supports reproducible debugging and audit trails.

---

## 4. Flags

- **`--dry-run`** — simulate execution without running commands  
- **`--log`** — write results to `/var/log/update.log`  
- **`--hashmap`** — generate traceability artefacts  

---

## 5. Output

### 📄 Log File  
`/var/log/update.log`  
Contains:

- executed update steps  
- locate database refresh output  
- timestamped summary block  

### 🧾 Hashmap Files  
Stored in `.hashmap/`:

- `update.hash` — SHA‑256 hash of the script  
- `update.timestamp` — execution timestamp  

---

## 6. Educational Notes

This tool demonstrates how **system maintenance automation** can be structured cleanly using Bash:

- ordered update sequences  
- dependency repair  
- cache cleanup  
- locate database refresh  
- reproducible traceability  

It is intentionally minimal and ideal for teaching system maintenance workflows.

---

## 7. Closure

This tool and its documentation were co‑authored with AI assistance.  
For responsible use, authorship transparency, and ethical notes, see the Toolbox README.

🔙 Return to **Toolbox**

---
