# 🛠️ fki — Full Kali Install

`fki` is a streamlined installer designed for users starting from the **minimal Kali Linux ISO**.  
It installs the complete, lean, VM‑friendly **kali‑linux‑large** environment in one command, giving you a fully functional Kali desktop without the bloat of the “everything” meta‑package.

This tool is ideal for new users, virtual machines, and anyone who wants a clean, predictable, operator‑grade Kali setup.

---

## 🎯 Purpose

`fki` provides a simple, reliable path to a full Kali installation by:

- Installing the recommended **kali‑linux‑large** meta‑package  
- Ensuring a complete desktop environment  
- Avoiding unnecessary tools and bloat  
- Providing a consistent, repeatable setup process  
- Integrating cleanly with the Toolbox workflow  

It is the final step in the 6‑step installation sequence described below.

---

# 🚀 The 6‑Step Kali Installation Path  
*A clean, fast, beginner‑friendly route to a full Kali environment*

This is the workflow you designed — the one you wish you’d had when you first started.

### **1) Download the Minimal Kali ISO**
Get the official minimal installer from Kali.org.  
This gives you a lightweight base system without preinstalled tools.

### **2) Copy the Toolbox Tools**
After installation, copy your Toolbox scripts into:

```
/usr/local/bin/bash
```

This keeps everything organised and consistent.

### **3) Add Toolbox to Your PATH**
Edit your `.bashrc`:

```bash
nano ~/.bashrc
```

Add:

```bash
export PATH="/usr/local/bin/bash:$PATH"
```

Reload:

```bash
source ~/.bashrc
```

### **4) Run the Toolbox Update Tool**
Before installing anything large, refresh the system:

```bash
sudo update
```

This ensures your base system is clean and current.

### **5) Run fki to Install the Full Kali Environment**
This installs the recommended, lean, complete desktop:

```bash
sudo fki
```

It uses:

```
kali-linux-large
```

…which is ideal for VMs and 8GB systems.

### **6) Run Update Again**
After installation, refresh everything one more time:

```bash
sudo update
```

Your system is now fully ready.

---

# 🧪 Usage

### Basic Installation
```bash
fki
```

This installs the full Kali environment using the `kali-linux-large` meta‑package.

---

# 🧩 What fki Installs

| Component | Description |
|----------|-------------|
| `kali-linux-large` | Full desktop environment + core Kali tools |
| Desktop | Default Kali desktop (XFCE unless changed) |
| System Tools | Networking, forensics, analysis, and admin tools |
| VM‑Friendly Footprint | Leaner than “everything”, ideal for 8GB RAM |

---

# 📁 Output

`fki` does not generate log files.  
All installation output is printed directly to the console.

---

# 🛡️ Ethical Scope

This tool performs **standard system installation only**.  
It does **not** perform scanning, enumeration, exploitation, or offensive actions.

It is intended for:

- learning  
- training  
- research  
- authorised environments  

---

# 🧠 Contributor Notes

- `fki` replaces the older `tool-fki` script  
- Versioning follows the Toolbox standard:  
  ```
  YYYY.MM.DD-BUILD
  ```
- The tool assumes the user has already run the Toolbox `update` tool  
- Designed for minimal ISO → full desktop workflows  
- Ideal for Hyper‑V, VirtualBox, VMware, and bare‑metal installs  

---

## 🤖 AI & Ethics Disclosure  

This tool and documentation were co‑authored with AI assistance.  
For details on ethical integration and responsible authorship, see:  
**ethics_AI.md** (github.com in Bing) (bing.com in Bing)

🔙 Return to Toolbox (bing.com in Bing)
