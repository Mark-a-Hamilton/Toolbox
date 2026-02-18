# 🧰 Toolbox — Defensive Operator Suite

**Toolbox** is a modular, operator‑grade collection of Bash and Python utilities designed for **incident response, diagnostics, system hygiene, and safe remote operations** on Ubuntu‑based environments.

It provides a curated, predictable workflow for:

- analysing and repairing Linux systems  
- maintaining system hygiene and stability  
- performing diagnostics and state checks  
- repairing broken sessions (GNOME/RDP)  
- verifying PostgreSQL service health  
- safely transferring and executing files during IR  
- generating hashes for chain‑of‑custody  
- running domain connectivity checks  
- performing safe, controlled injection scanning  
- generating VyOS zone‑pair configurations  

Toolbox is **not** a penetration‑testing framework.  
It is a **defensive, blue‑team‑focused toolkit** designed for clarity, safety, and operational maturity.

---

# 📖 Project Overview

Toolbox provides:

- A **clean, reproducible workflow** for maintaining Ubuntu‑based systems  
- A set of **modular tools** for diagnostics, cleanup, hashing, session repair, and safe remote execution  
- A **consistent architecture** with metadata, versioning, and documentation  
- A **professional, operator‑grade layout** suitable for IR teams and system maintainers  

Every tool is:

- versioned using the `YYYY.MM.DD-BUILD` model  
- documented in `/docs`  
- traceable via optional hash‑map generation  
- globally accessible when placed in the Toolbox tool paths  

---

# 🔧 Toolbox Tool Paths

Toolbox supports tools written in **Bash**, **Python**, and **PHP**.  
Each language has its own dedicated directory under `/usr/local/bin` for consistency and predictability.

| Language | Path |
|----------|------|
| **Bash**   | `/usr/local/bin/bash` |
| **Python** | `/usr/local/bin/python` |
| **PHP**    | `/usr/local/bin/php` |

These paths are used by:

- the **tool‑box** indexer  
- your **PATH** configuration  
- your **documentation structure**  
- your **metadata conventions**  

---

# 🧩 Adding Toolbox Paths to Your Shell

Add to `~/.bashrc`:

```bash
export PATH="/usr/local/bin/bash:/usr/local/bin/python:/usr/local/bin/php:$PATH"
```

Reload:

```bash
source ~/.bashrc
```

---

# 🚀 Getting Started

### **1) Install Toolbox directories**
```bash
sudo mkdir -p /usr/local/bin/bash
sudo mkdir -p /usr/local/bin/python
sudo mkdir -p /usr/local/bin/php
```

### **2) Copy tools into place**
```bash
sudo cp bash/* /usr/local/bin/bash
sudo cp python/* /usr/local/bin/python
sudo cp php/* /usr/local/bin/php
sudo chmod +x /usr/local/bin/bash/*
sudo chmod +x /usr/local/bin/python/*
sudo chmod +x /usr/local/bin/php/*
```

### **3) Add Toolbox to PATH**
```bash
export PATH="/usr/local/bin/bash:/usr/local/bin/python:/usr/local/bin/php:$PATH"
source ~/.bashrc
```

You now have a clean, defensive operator toolbox ready for use.

---

# 📁 Folder Structure

| Folder        | Description                                                                 |
|---------------|-----------------------------------------------------------------------------|
| `docs/`       | Documentation for each tool and workflow                                    |
| `bash/`       | Bash tools (installed to `/usr/local/bin/bash`)                             |
| `python/`     | Python tools (installed to `/usr/local/bin/python`)                         |
| `php/`        | PHP tools (installed to `/usr/local/bin/php`)                               |
| `.hashmap/`   | Optional folder for script hashes and timestamps                            |
| `assets/`     | Diagrams, screenshots, and visual aids                                      |

---

# 🧩 Key Tools

| Tool      | Purpose |
|-----------|---------|
| `update`  | System update + locate DB refresh |
| `cleanup` | System hygiene and temporary file cleanup |
| `diag`    | Diagnostics and environment checks |
| `lstnr`   | Ethical listener with safe fallback |
| `hash`    | MD5 hash creation and verification |
| `pgsql-session` | PostgreSQL session wrapper |
| `pgsql-state`   | PostgreSQL service state checker |
| `repsess` | Repair broken GNOME/RDP sessions |
| `xfer`    | Safe remote transfer + execution utility |
| `bf`      | Pattern‑based brute‑force demonstrator (educational) |
| `domcon`  | Domain connectivity preflight checker |
| `is`      | Injection scanner engine |
| `zpg`     | VyOS zone‑pair generator |

Full documentation for each tool is in `/docs`.

---

# 🛡️ Defensive Philosophy

Toolbox is designed around **blue‑team principles**:

### **1. Safety & Control**
All tools operate under:

- authenticated  
- bounded  
- predictable  
- auditable  

execution models.

### **2. No Offensive Capability**
Toolbox contains **no red‑team tools**, payloads, or exploitation mechanisms.

### **3. Transparency**
Every tool includes:

- version metadata  
- purpose metadata  
- optional hash‑based traceability  

### **4. Responsible Use**
Toolbox is intended for:

- incident response  
- diagnostics  
- system repair  
- safe remote operations  
- educational demonstrations  

Use only in environments where you have explicit permission.

---

# 🤝 Contributing

Contributions are welcome. Please ensure:

- tools follow the `template` structure  
- versioning uses `YYYY.MM.DD-BUILD`  
- documentation is added to `/docs`  
- functionality remains within the defensive scope  

---

# 📜 License

This project is licensed under the [MIT License](https://github.com/Mark-a-Hamilton/Toolbox/blob/main/LICENSE)
