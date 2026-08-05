# 📘 **ba — Boot‑Up Analysis Tool**

## 1. Introduction

`ba` is a lightweight, structured **Linux boot‑analysis tool** designed for controlled environments, lab systems, and diagnostic workflows inside the Toolbox ecosystem.

It performs a complete inspection of the **systemd boot process**, capturing:

- user manager service health  
- boot summary timing  
- critical‑chain dependency delays  
- running job lists  
- blame metrics for slow units  

The tool is ideal for:

- validating boot performance  
- diagnosing slow or failing services  
- generating logs for AI‑assisted analysis  
- producing traceability artefacts for reproducible debugging  

---

## 2. Usage

```bash
ba [--dry-run] [--verbose] [--log] [--hashmap]
```

The tool runs interactively and prints progress to the terminal while optionally writing structured output to `/var/log/ba.log`.

---

## 3. Features

### 🔍 Boot Summary Extraction  
Captures the full `systemd-analyze` summary, including total boot time and breakdown of kernel vs userspace.

### 🧩 Critical‑Chain Analysis  
Identifies slow or blocking units in the boot dependency chain.

### 📋 Job Enumeration  
Lists currently running systemd jobs to highlight stuck or long‑running operations.

### ⚠️ Blame Metrics  
Displays per‑unit timing information to pinpoint slow services.

### 🧪 Dry‑Run Mode  
Simulates execution without running commands — ideal for testing or CI pipelines.

### 🗂️ Hashmap Traceability  
Generates SHA‑256 hashes and timestamps for reproducible analysis.

---

## 4. Flags

- **`--dry-run`** — simulate execution without running commands  
- **`--verbose`** — print detailed execution logs  
- **`--log`** — write results to `/var/log/ba.log`  
- **`--hashmap`** — generate `.hashmap/ba.hash` and `.hashmap/ba.timestamp`  

---

## 5. Output

### 📄 Log File  
`/var/log/ba.log`  
Contains the full boot analysis including:

- user manager service status  
- boot summary  
- critical chain  
- job list  
- blame metrics  
- execution metadata  

### 🧾 Hashmap Files  
Stored in `.hashmap/`:

- `ba.hash` — SHA‑256 hash of the script  
- `ba.timestamp` — execution timestamp  

These files support reproducible debugging and traceability across runs.

---

## 6. Educational Notes

This tool demonstrates how **systemd boot diagnostics** can be automated and structured for repeatable analysis. It highlights:

- how dependency chains affect boot performance  
- how slow units propagate delays  
- how job lists reveal stuck services  
- how blame metrics guide remediation  

It is intentionally minimal, transparent, and ideal for teaching boot‑process forensics.

---

## 7. Closure

This tool and its documentation were co‑authored with AI assistance.  
For responsible use, authorship transparency, and ethical notes, see the Toolbox README.

🔙 Return to **Toolbox**

---
