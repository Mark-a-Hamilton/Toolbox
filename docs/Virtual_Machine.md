# 🖥️ Virtual Machine — Creating a Kali Environment on Windows

`VirtualMachine` is the starting point for new users who want to run Kali Linux on a Windows host.  
This guide walks through creating a Kali environment using either **Hyper‑V** or **WSL**, then hands off to the `fki` workflow to complete the installation.

It is designed as a deliberate, indexed entry point into the Toolbox ecosystem.

---

## 🎯 Purpose

This document provides a clear, tested path to:

- Create a Kali environment on a Windows machine  
- Use either **Hyper‑V** (full VM) or **WSL** (lightweight subsystem)  
- Prepare the system for Toolbox tools  
- Hand off cleanly to the **Full Kali Install** process via `fki.md`  

It is written for users who may be completely new to Linux.

---

# 🧱 Option 1 — Hyper‑V Kali Virtual Machine

### 1. Enable Hyper‑V (if not already enabled)

On Windows:

1. Open **Control Panel → Programs → Turn Windows features on or off**
2. Enable:
   - **Hyper‑V**
   - **Virtual Machine Platform**
3. Reboot when prompted.

### 2. Download the Kali Minimal ISO

From the official Kali website, download the **minimal installer ISO**.

Save it somewhere accessible from your Windows host (e.g. `C:\ISOs\kali-minimal.iso`).

### 3. Create a New Hyper‑V VM

1. Open **Hyper‑V Manager**
2. Click **New → Virtual Machine**
3. Recommended settings:
   - **Generation:** 2
   - **Memory:** at least **4 GB** (8 GB preferred)
   - **Network:** attach to a virtual switch with internet access
   - **Virtual hard disk:** at least **60 GB**
4. When asked for an installation source, select:
   - **Image file (.iso)** → browse to your Kali minimal ISO

Finish the wizard and start the VM.

### 4. Install Kali (Minimal)

Inside the VM:

1. Boot from the ISO
2. Follow the Kali installer
3. Choose a minimal installation (no extra tools)
4. Create a user and password
5. Complete the install and reboot into your new Kali system

Once you can log into Kali, you’re ready for Toolbox.

---

# 🧩 Option 2 — WSL Kali Environment

> Note: WSL is lighter than a full VM and does not provide a full desktop environment by default. It’s ideal for CLI‑focused workflows.

### 1. Enable WSL

In an elevated PowerShell:

```powershell
wsl --install
```

Reboot if prompted.

### 2. Install Kali via WSL

In PowerShell:

```powershell
wsl --install -d kali-linux
```

Once installed, launch Kali from the Start menu or via:

```powershell
wsl -d kali-linux
```

Create your user when prompted.

You now have a Kali environment inside WSL.

---

# 🧰 Next Step — Install the Toolbox and Run fki

Once your Kali environment exists (Hyper‑V or WSL), the next steps are the same.

### 1. Copy Toolbox Tools

Inside Kali, create a Toolbox directory:

```bash
sudo mkdir -p /usr/local/bin/bash
```

Copy your Toolbox scripts (including `update`, `fki`, etc.) into:

```bash
/usr/local/bin/bash
```

Ensure they are executable:

```bash
sudo chmod +x /usr/local/bin/bash/*
```

### 2. Add Toolbox to PATH

Edit your shell config:

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

### 3. Follow the Full Kali Install Guide

From here, follow the deliberate workflow documented in:

- **`fki.md` — Full Kali Install**

In short:

1. Run:
   ```bash
   sudo update
   ```
2. Then:
   ```bash
   sudo fki
   ```
3. Finally:
   ```bash
   sudo update
   ```

This sequence gives you a clean, fully functional Kali environment with a curated toolset.

---

## 🧭 How This Fits into the Toolbox

- `VirtualMachine.md` → helps you **create** the environment  
- `fki.md` → helps you **populate** it with a full Kali install  
- `update` → keeps it **maintained**  
- Other tools → layer on diagnostics, hygiene, listeners, etc.

This is the intentional, repeatable path into your ecosystem.

---

## 🤖 AI & Ethics Disclosure  

This guide was co‑authored with AI assistance.  
For details on ethical integration, traceability, and responsible authorship, see `ethics_AI.md`.

🔙 Return to [Toolbox](https://github.com/Mark-a-Hamilton/Toolbox)
