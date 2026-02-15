# 🧹 cleanup

`cleanup` is a modular system‑hygiene tool within the Toolbox suite.  
It performs safe maintenance operations—removing unused packages, clearing caches, and cleaning temporary files—with optional dry‑run simulation, logging, and hash‑based audit support.

---

## 🎯 Purpose

`cleanup` helps maintain system hygiene and operational readiness by:

- Removing orphaned or unused packages  
- Clearing package caches  
- Cleaning temporary directories  
- Logging actions with timestamps  
- Generating SHA‑256 hashes for audit traceability  

Designed for Debian‑based systems (Ubuntu, Debian, Kali, etc.), it provides a predictable, operator‑friendly maintenance workflow.

---

## 🧪 Usage

### Basic Cleanup
```bash
cleanup
```
Executes all cleanup steps.

### Dry‑Run Mode
```bash
cleanup --dry-run
```
Simulates each step without making changes.

### Logging Mode
```bash
cleanup --log
```
Writes execution details to:
```
/var/log/cleanup.log
```

### Hash‑Based Audit Mode
```bash
cleanup --hashmap
```
Creates:
```
.hashmap/cleanup.hash
.hashmap/cleanup.timestamp
```

---

## 🧩 Parameters

| Flag         | Description                                      |
|--------------|--------------------------------------------------|
| `--dry-run`  | Simulates cleanup steps without executing        |
| `--log`      | Logs actions to `/var/log/cleanup.log`           |
| `--hashmap`  | Stores script hash and timestamp in `.hashmap/`  |
| `--help`     | Displays usage instructions                      |

---

## 🔧 Steps Performed

| Command                 | Description                               |
|-------------------------|-------------------------------------------|
| `apt autoremove -y`     | Removes orphaned or unused packages       |
| `apt clean`             | Clears package cache                      |
| `rm -rf /var/cache/apt/*` | Removes cached package metadata         |
| `rm -rf /tmp/*`         | Cleans temporary files                    |

---

## 📁 Output

### Console Output
- Confirmation of each executed or simulated step  
- Clear indication of dry‑run vs. live execution  

### Optional Files
| File Path                     | Purpose                          |
|-------------------------------|----------------------------------|
| `/var/log/cleanup.log`        | Timestamped cleanup log          |
| `.hashmap/cleanup.hash`       | SHA‑256 hash of the script       |
| `.hashmap/cleanup.timestamp`  | Timestamp of hash generation     |

All output locations are explicitly shown during execution.

---

## 📢 Disclaimer

This tool performs **non‑destructive system hygiene only**.  
It does **not** perform scanning, enumeration, or offensive actions.  
Use responsibly and only in environments where you have explicit permission.

---

## 🤖 AI & Ethics Disclosure  

This tool was co‑authored with AI assistance.  
For full details on ethical integration, traceability, and responsible authorship, see:  
ethics_AI.md (github.com in Bing) (bing.com in Bing) [(bing.com in Bing)](https://www.bing.com/search?q="https%3A%2F%2Fwww.bing.com%2Fsearch%3Fq%3D%2522https%253A%252F%252Fgithub.com%252FMark-a-Hamilton%252FMark-a-Hamilton.github.io%252Fblob%252Fmain%252Fethics_AI.md%2522")

🔙 Return to [Toolbox](https://github.com/Mark-a-Hamilton/Toolbox)
