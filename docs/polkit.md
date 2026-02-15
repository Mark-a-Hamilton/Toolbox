# 🔐 polkit — Polkit Service Toggle  
*A controlled way to enable or disable the system’s privilege‑escalation broker*

`polkit` is a lightweight operator tool that toggles the **polkit** service between active and inactive states.  
It allows you to keep your system lean and locked down when polkit is not required, while enabling it on‑demand for tasks that rely on GUI‑based or service‑mediated privilege escalation.

This document explains what polkit is, why it matters, and how this tool manages it safely.

---

# 🧩 What Is Polkit?

**Polkit (formerly PolicyKit)** is a system service used by Linux desktops to manage *privilege escalation* for applications that are **not running as root**.

It acts as a **broker** between:

- unprivileged processes  
- privileged system services  
- user authentication mechanisms  

In practice, polkit enables things like:

- graphical “Authentication Required” prompts  
- allowing a non‑root user to restart services  
- enabling system settings changes from the GUI  
- authorising package installs from graphical tools  
- allowing network configuration changes  
- enabling power‑management actions (shutdown, reboot, suspend)  

Without polkit:

- GUI tools cannot request elevated privileges  
- many desktop actions silently fail  
- system settings may become read‑only  
- privilege escalation must be done manually (sudo, su, etc.)

For **server**, **DFIR**, **lab**, or **minimal VM** environments, polkit is often unnecessary and can be safely disabled.

For **desktop** environments, polkit is usually required.

This tool gives you **operator‑grade control** over when polkit is active.

---

# 🎯 Purpose of the `polkit` Tool

This tool provides a predictable way to:

- **stop and mask** polkit when not needed  
- **unmask and start** polkit when required  
- ensure the system remains lean, quiet, and secure  
- avoid unnecessary background services  
- reduce attack surface on minimal or DFIR systems  

It is especially useful when:

- running a hardened or minimal Ubuntu/Kali VM  
- performing DFIR work where privilege brokers are unnecessary  
- reducing noise and background processes  
- controlling when GUI privilege escalation is allowed  
- preparing a clean environment for forensic analysis  

---

# 🛠️ Usage

```
sudo polkit [--dry-run] [--verbose]
```

### Examples

```
sudo polkit
sudo polkit --dry-run
sudo polkit --verbose
```

---

# ⚙️ What the Tool Actually Does

The tool performs a controlled toggle based on the current state of the service:

### **1. If polkit is active**
It will:

- stop the service  
- mask it (prevent auto‑start)  

### **2. If polkit is masked**
It will:

- unmask the service  
- start it  

### **3. If polkit is inactive but not masked**
It will:

- simply start the service  

This ensures predictable behaviour in all scenarios.

---

# 🧭 Expected Output

### **Stopping and masking**
```
[polkit] Polkit stopped and masked.
```

### **Unmasking and starting**
```
[polkit] Polkit unmasked and started.
```

### **Starting when inactive**
```
[polkit] Polkit started.
```

### **Dry‑run mode**
```
[DRY-RUN] systemctl stop polkit.service
```

---

# 🧩 When You Should Use This Tool

### ✔ Minimal or hardened systems  
Disable polkit to reduce attack surface and background processes.

### ✔ DFIR environments  
Avoid privilege brokers that may interfere with evidence or logs.

### ✔ Lab VMs  
Keep the system lightweight and predictable.

### ✔ When GUI privilege escalation is temporarily required  
Enable polkit only when needed.

### ✔ When troubleshooting desktop privilege issues  
If GUI tools fail to escalate privileges, polkit may be masked or inactive.

---

# 🩺 Troubleshooting

### **GUI tools fail to escalate privileges**
Run:

```
sudo polkit
```

This will unmask and start the service.

---

### **System settings appear locked or read‑only**
Polkit may be masked.

---

### **Service fails to start**
Check logs:

```
sudo journalctl -u polkit.service
```

---

### **Systemd reports “masked”**
Unmask it:

```
sudo systemctl unmask polkit.service
```

---

# 🔗 Related Tools

| Tool | Purpose |
|------|---------|
| `diag` | System diagnostics and environment checks |
| `cleanup` | System hygiene and temporary file cleanup |
| `update` | Package updates and locate DB refresh |
| `repsess` | Repairs broken GNOME/RDP sessions |
| `xfer` | Remote transfer + execution utility |

---

## 🤖 AI & Ethics Disclosure

This tool and its documentation were co‑authored with AI assistance.  
For details on responsible use, transparency, and authorship, see the **AI & Ethics** section in the Toolbox README.

🔙 Return to Toolbox [(github.com in Bing)](https://www.bing.com/search?q="https%3A%2F%2Fgithub.com%2FMark-a-Hamilton%2FToolbox")
  
- or the next documentation page in your queue  

Just tell me which one you want to tackle next.
