# 📘 **mda4w — Windows Memory Dump Analysis Tool**

## 1. Introduction

`mda4w` is a lightweight, operator‑friendly wrapper around **Volatility3**, designed to streamline the analysis of Windows memory dumps.  
It runs a curated set of Windows‑specific plugins and stores each result in a structured output directory for easy review.

This tool is intentionally minimal:

- **no noise**  
- **no assumptions**  
- **no unnecessary automation**  
- **just clean, structured output**  

It is ideal for:

- THM rooms involving memory forensics  
- DFIR practice  
- malware analysis  
- incident response  
- CTF challenges  
- general Windows memory triage  

---

## 2. Features

### ✔ Minimal, predictable behaviour  
Runs a fixed set of Volatility3 plugins known to provide high‑value forensic insight.

### ✔ Clean output structure  
All results are stored in:

```
mda4w-output/
```

Each plugin produces a single `.out` file.

### ✔ Safe and non‑destructive  
The tool never modifies the memory dump.  
It only reads and extracts information.

### ✔ Works anywhere  
As long as Volatility3 is installed, `mda4w` works from any directory.

### ✔ Perfect for THM workflows  
Memory forensics rooms often require:

- process enumeration  
- driver inspection  
- network artefacts  
- file object scanning  
- SID and handle analysis  

This tool automates the repetitive part so you can focus on the analysis.

---

## 3. Dependencies

`mda4w` requires:

### **Volatility3**
Installed on Kali by default, or install manually:

```
sudo apt install volatility3
```

or via pip:

```
pip install volatility3
```

### **Bash**
The tool is written in Bash and works on:

- Kali Linux  
- Ubuntu  
- Debian  
- WSL  
- Any Linux environment with Volatility3  

---

## 4. Installation

Place the script in your toolbox directory or system path:

```
/usr/local/bin/mda4w
```

Make it executable:

```
chmod +x /usr/local/bin/mda4w
```

You can now run it from anywhere.

---

## 5. Usage

### Basic usage

```
mda4w <memory_dump>
```

### With Volatility flags

```
mda4w <memory_dump> -f
```

### Example

```
mda4w memdump.mem -f
```

This will:

- create `mda4w-output/`
- run all selected plugins
- save each result as `<plugin>.out`
- print a summary of what each file contains

---

## 6. Output Structure

After running the tool, you will see:

```
mda4w-output/
├── cmdline.out
├── drivermodule.out
├── filescan.out
├── getsids.out
├── handles.out
├── info.out
├── netscan.out
├── netstat.out
├── mftscan.out
├── pslist.out
└── pstree.out
```

Each file corresponds to a Volatility3 plugin.

---

## 7. Plugin Overview

| Plugin | Purpose |
|--------|---------|
| **cmdline** | Lists process command‑line arguments |
| **drivermodule** | Detects hidden or suspicious drivers |
| **filescan** | Scans for file objects in memory |
| **getsids** | Shows SIDs associated with each process |
| **handles** | Lists open handles per process |
| **info** | Displays OS and kernel details |
| **netscan** | Scans for network objects |
| **netstat** | Traverses network tracking structures |
| **mftscan** | Scans for MFT entries and ADS |
| **pslist** | Lists running processes |
| **pstree** | Shows parent/child process relationships |

These plugins provide a strong baseline for Windows memory triage.

---

## 8. Example Workflow (THM‑Style)

1. Recover the memory dump from the target  
2. Run:

   ```
   mda4w memdump.mem -f
   ```

3. Review:

   - `pslist.out` → suspicious processes  
   - `drivermodule.out` → hidden drivers  
   - `netscan.out` → active connections  
   - `filescan.out` → dropped malware  
   - `mftscan.out` → ADS or hidden files  
   - `cmdline.out` → malicious command lines  

4. Build your narrative or answer room questions  
5. Use the structured output to support your findings  

This workflow is fast, clean, and repeatable.

---

## 9. Philosophy

`mda4w` follows the same principles as the rest of your toolbox:

### **Minimal requests**  
Only the essential plugins are executed.

### **Maximum analysis**  
Each plugin produces high‑value forensic artefacts.

### **Zero noise**  
No unnecessary output, no clutter.

### **Operator‑friendly**  
You stay in control of the analysis.

### **Educational**  
The tool teaches you how memory forensics works by exposing the raw artefacts.

---

## 10. Summary

`mda4w` is a compact, efficient, and reliable Windows memory analysis tool that:

- automates repetitive Volatility3 tasks  
- produces clean, structured output  
- supports DFIR, THM rooms, and real‑world analysis  
- fits perfectly into your minimalist, operator‑grade toolbox  

It’s a small script with outsized impact — exactly the kind of tool that makes your toolbox powerful.

