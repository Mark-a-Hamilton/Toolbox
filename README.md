Absolutely, Mark — here is the **fully merged, polished, ready‑to‑paste README.md**, now including:

- the **updated Toolbox identity**
- the **AI & Ethics section**
- the **multi‑language tool paths** (bash, python, php)
- the **6‑step installation workflow**
- the **VM creation entry point**
- the **modernised structure** that matches your new ecosystem

This is a complete drop‑in replacement for your current README.

---

# 🧰 Toolbox

**Toolbox** is a modular, operator‑grade suite of Bash, Python, and PHP utilities designed to create, maintain, and evolve a clean, predictable Linux environment — with a special focus on Kali and Debian‑based systems.

It provides a curated workflow for:

- building a new Kali environment (VM or WSL)  
- installing a full desktop and toolset  
- maintaining system hygiene  
- performing updates, diagnostics, and cleanup  
- ensuring traceability and ethical clarity  

Toolbox is **not** a penetration‑testing framework.  
It is a **system‑maintenance and environment‑building toolkit**.

---

## 📖 Project Overview

Toolbox provides:

- A **deliberate, reproducible workflow** for setting up a full Kali environment  
- A set of **modular tools** for updates, cleanup, diagnostics, listeners, and installation  
- A **clean architecture** with consistent metadata, versioning, and documentation  
- A **beginner‑friendly path** from minimal ISO → full Kali desktop → maintained system  

Every tool is:

- versioned using the `YYYY.MM.DD-BUILD` model  
- documented in `/docs`  
- traceable via optional hash‑map generation  
- globally accessible when placed in the Toolbox tool paths  

---

# 🔧 Toolbox Tool Paths (Bash, Python, PHP)

Toolbox supports tools written in **Bash**, **Python**, and **PHP**.  
To keep everything consistent, predictable, and easy to index, each language has its own dedicated directory under `/usr/local/bin`.

### **Standardised Tool Locations**

| Language | Path |
|----------|------|
| **Bash**   | `/usr/local/bin/bash` |
| **Python** | `/usr/local/bin/python` |
| **PHP**    | `/usr/local/bin/php` |

These paths are used by:

- the **tool‑box** indexer  
- your **PATH** configuration  
- your **documentation structure**  
- your **versioning and metadata conventions**  

This ensures every tool—regardless of language—behaves the same way.

---

## 🧩 Adding Toolbox Paths to Your Shell

Add the following to your `~/.bashrc`:

```bash
export PATH="/usr/local/bin/bash:/usr/local/bin/python:/usr/local/bin/php:$PATH"
```

Reload:

```bash
source ~/.bashrc
```

This makes all Toolbox tools globally available.

---

# 🚀 Getting Started (The Toolbox Workflow)

Toolbox provides a **6‑step, beginner‑friendly path** to a full Kali environment.

### **1) Create a Kali VM (Hyper‑V or WSL)**  
See:  
📄 `docs/VirtualMachine.md`

### **2) Copy Toolbox tools into place**
```bash
sudo mkdir -p /usr/local/bin/bash
sudo mkdir -p /usr/local/bin/python
sudo mkdir -p /usr/local/bin/php
sudo cp <your toolbox scripts> /usr/local/bin/bash
sudo chmod +x /usr/local/bin/bash/*
```

### **3) Add Toolbox to your PATH**
Add to `~/.bashrc`:
```bash
export PATH="/usr/local/bin/bash:/usr/local/bin/python:/usr/local/bin/php:$PATH"
```
Reload:
```bash
source ~/.bashrc
```

### **4) Run the update tool**
```bash
sudo update
```

### **5) Run the Full Kali Installer**
```bash
sudo fki
```

### **6) Run update again**
```bash
sudo update
```

You now have a clean, complete, reproducible Kali environment.

---

# 📁 Folder Structure

| Folder        | Description                                                                 |
|---------------|-----------------------------------------------------------------------------|
| `docs/`       | Documentation for each tool and workflow                                    |
| `bash/`       | Toolbox Bash scripts (installed to `/usr/local/bin/bash`)                   |
| `python/`     | Toolbox Python scripts (installed to `/usr/local/bin/python`)               |
| `php/`        | Toolbox PHP scripts (installed to `/usr/local/bin/php`)                     |
| `.hashmap/`   | Optional folder for script hashes and timestamps                            |
| `assets/`     | Diagrams, screenshots, and visual aids                                      |

---

# 🧩 Key Tools

| Tool      | Purpose |
|-----------|---------|
| `update`  | Full system update + locate DB refresh |
| `cleanup` | System hygiene and temporary file cleanup |
| `diag`    | Diagnostics and environment checks |
| `lstnr`   | Ethical listener with socat/netcat fallback |
| `fki`     | Full Kali Install (kali‑linux‑large) |
| `template`| Base template for creating new tools |

Full documentation for each tool is in `/docs`.

---

# 🤖 AI & Ethics

Toolbox is co‑developed with AI assistance.  
To ensure transparency, safety, and responsible use, the project follows these principles:

### **1. Ethical Boundaries**
Toolbox contains **no offensive security tools**.  
All scripts wrap standard system commands for maintenance and setup.

### **2. Transparency**
Every tool includes:

- version metadata  
- purpose metadata  
- optional hash‑based traceability  

### **3. Responsible AI Use**
AI is used for:

- documentation  
- code generation  
- workflow refinement  

…but all output is reviewed, tested, and validated by a human operator.

### **4. User Responsibility**
Use Toolbox only in environments where you have explicit permission.  
It is designed for learning, maintenance, and operational hygiene.

---

# 🤝 Contributing

Contributions are welcome. Please ensure:

- tools follow the `template` structure  
- versioning uses `YYYY.MM.DD-BUILD`  
- documentation is added to `/docs`  
- functionality remains within the ethical scope  

---

# 📜 License

This project is licensed under the [MIT License](https://github.com/Mark-a-Hamilton/Toolbox/edit/main/LICENSE)
