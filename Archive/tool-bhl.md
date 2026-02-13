# 🧠 tool-bhl

`tool-bhl` is a modular launcher for BloodHound and Neo4j on Kali Linux. It handles privilege separation, service diagnostics, and optional dry-run and audit logging for ethical and traceable usage.

---

## 🎯 Purpose

This tool simplifies launching BloodHound and Neo4j by:

- Checking service status and user context
- Starting Neo4j and BloodHound with privilege awareness
- Supporting dry-run simulation and verbose output
- Logging launch actions and generating audit hashes

---

## 🚀 Usage

### Launch BloodHound + Neo4j
```bash
tool-bhl
```

### Dry-Run Mode
```bash
tool-bhl --dry-run
```

### Verbose Output
```bash
tool-bhl --verbose
```

### With Hash-Based Audit
```bash
tool-bhl --hashmap
```

---

## ⚙️ Parameters

| Flag         | Description                                      |
|--------------|--------------------------------------------------|
| `--dry-run`  | Simulates launch steps without executing         |
| `--verbose`  | Displays detailed output during launch           |
| `--hashmap`  | Stores script hash and timestamp in `.hashmap/`  |
| `--help`     | Displays usage instructions                      |

---

## 🔍 Diagnostics

- Verifies Neo4j service status
- Checks for BloodHound binary presence
- Detects privilege context and suggests elevation if needed

---

## 📁 Output

- Console summary of launch steps
- Optional `.hashmap/` entry for audit traceability
- Exit codes for success/failure diagnostics

---

## 🤖 AI & Ethics Disclosure  

This tool was co-authored with AI assistance. For full details on ethical integration, traceability, and responsible authorship, see [ethics_AI.md]([https://mark-a-hamilton.github.io/main/ethics_AI.md](https://github.com/Mark-a-Hamilton/Mark-a-Hamilton.github.io/blob/main/ethics_AI.md)).  
🔙 [Return to Kali-toolbox](https://github.com/Mark-a-Hamilton/kali-toolbox)
