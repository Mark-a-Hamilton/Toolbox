# 📘 **ldp — Linux Desktop Launcher (X11 / D‑Bus / XFCE)**

## 1. Introduction

`ldp` is a lightweight Toolbox module that launches a **fully functional Linux desktop session** using X11, D‑Bus, and XFCE. It is designed for controlled lab environments, remote‑desktop workflows, and PrivEsc training setups where a predictable, reproducible desktop startup sequence is required.

It performs:

- X11 backend configuration  
- D‑Bus session initialisation  
- ICE socket permission correction  
- XFCE session lock cleanup  
- window manager startup (`xfwm4`)  
- full XFCE session launch  
- optional logging + traceability  

This tool is ideal for:

- repairing broken XFCE sessions  
- launching desktops inside RDP/VNC containers  
- validating X11 rendering paths  
- ensuring consistent GUI startup in lab systems  

---

## 2. Usage

```bash
ldp [--dry-run] [--verbose] [--log] [--hashmap]
```

The tool prints progress to the terminal and optionally writes structured output to `/var/log/ldp.log`.

---

## 3. Features

### 🖥️ X11 Rendering Setup  
Configures X11 backend variables:

- `LIBGL_ALWAYS_INDIRECT=1`  
- `GDK_BACKEND=x11`  
- `QT_QPA_PLATFORM=xcb`  

Ensures compatibility with remote desktop environments.

### 🔔 D‑Bus Session Initialisation  
Starts a new D‑Bus session if none exists, ensuring desktop components can communicate correctly.

### ❄️ ICE Socket Permission Fix  
Corrects `/tmp/.ICE-unix` permissions to prevent session startup failures.

### 🔐 XFCE Session Lock Cleanup  
Removes stale lock files that can block new XFCE sessions.

### 🪟 Window Manager Startup  
Starts `xfwm4` if not already running, ensuring window decorations and focus behaviour work correctly.

### 🧪 Dry‑Run Mode  
Simulates execution without running commands — ideal for testing or CI pipelines.

### 🗂️ Hashmap Traceability  
Generates SHA‑256 hashes and timestamps for reproducible debugging.

---

## 4. Flags

- **`--dry-run`** — simulate execution without running commands  
- **`--verbose`** — print detailed execution logs  
- **`--log`** — write results to `/var/log/ldp.log`  
- **`--hashmap`** — generate `.hashmap/ldp.hash` and `.hashmap/ldp.timestamp`  

---

## 5. Output

### 📄 Log File  
`/var/log/ldp.log`  
Contains:

- X11 variable setup  
- D‑Bus session status  
- ICE socket correction  
- XFCE lock cleanup  
- window manager launch  
- full XFCE session startup  
- execution metadata  

### 🧾 Hashmap Files  
Stored in `.hashmap/`:

- `ldp.hash` — SHA‑256 hash of the script  
- `ldp.timestamp` — execution timestamp  

These files support reproducible debugging and traceability across runs.

---

## 6. Educational Notes

This tool demonstrates how **desktop session orchestration** can be automated cleanly using Bash:

- environment variable setup  
- session bus initialisation  
- permission correction  
- window manager lifecycle control  
- reproducible traceability  

It is intentionally minimal, transparent, and ideal for teaching GUI startup mechanics in Linux.

---

## 7. Closure

This tool and its documentation were co‑authored with AI assistance.  
For responsible use, authorship transparency, and ethical notes, see the Toolbox README.

🔙 Return to **Toolbox**

---

