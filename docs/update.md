 # 🔄 update

`update` is a modular system‑update utility within the Toolbox suite.  
It performs a full package refresh using `apt`, followed by a locate‑database rebuild for accurate file indexing. The tool supports dry‑run simulation, logging, and hash‑based traceability.

---

## 🎯 Purpose

`update` simplifies and standardises system maintenance by:

- Running `apt update`, `apt upgrade`, `apt autoremove`, and `apt clean`  
- Refreshing the locate database (`updatedb`)  
- Supporting dry‑run mode for safe previewing  
- Logging update actions with timestamps  
- Generating SHA‑256 hashes for audit traceability  

It provides a predictable, operator‑grade workflow for Debian‑based systems.

---

## 🧪 Usage

### Basic Update
```bash
sudo update
```

### Dry‑Run Mode
```bash
sudo update --dry-run
```
Simulates all update steps without making changes.

### Logging Mode
```bash
sudo update --log
```
Writes update actions to:
```
/var/log/update.log
```

### Hash‑Based Audit Mode
```bash
sudo update --hashmap
```
Creates:
```
.hashmap/update.hash
.hashmap/update.timestamp
```

---

## 🧩 Parameters

| Flag         | Description                                      |
|--------------|--------------------------------------------------|
| `--dry-run`  | Simulates update steps without executing         |
| `--log`      | Logs actions to `/var/log/update.log`            |
| `--hashmap`  | Stores script hash and timestamp in `.hashmap/`  |
| `--help`     | Displays usage instructions                      |

---

## 🔧 Steps Performed

| Command                   | Description                                      |
|---------------------------|--------------------------------------------------|
| `apt update`              | Refreshes package lists                          |
| `apt upgrade -y`          | Installs available updates                       |
| `apt autoremove -y`       | Removes unused dependencies                      |
| `apt clean`               | Clears cached package data                       |
| `updatedb --verbose`      | Rebuilds the locate database                     |
| `stat /var/lib/plocate/plocate.db` | Verifies database freshness            |

---

## 📁 Output Files

| File Path                     | Purpose                          |
|-------------------------------|----------------------------------|
| `/var/log/update.log`         | Timestamped update log           |
| `.hashmap/update.hash`        | SHA‑256 hash of the script       |
| `.hashmap/update.timestamp`   | Timestamp of update execution    |

All output locations are displayed during execution.

---

## 📢 Disclaimer

This tool performs **standard system maintenance only**.  
It does **not** perform scanning, enumeration, or offensive actions.  
Use responsibly and only in environments where you have explicit permission.

---

## 🤖 AI & Ethics Disclosure  

This tool was co‑authored with AI assistance.  
For full details on ethical integration, traceability, and responsible authorship, see:  
ethics_AI.md (github.com in Bing) (bing.com in Bing)

🔙 Return to Toolbox (bing.com in Bing) [(bing.com in Bing)](https://www.bing.com/search?q="https%3A%2F%2Fwww.bing.com%2Fsearch%3Fq%3D%2522https%253A%252F%252Fwww.bing.com%252Fsearch%253Fq%253D%252522https%25253A%25252F%25252Fgithub.com%25252FMark-a-Hamilton%25252FToolbox%252522%2522")
