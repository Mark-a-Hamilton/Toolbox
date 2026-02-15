# 🖥️ repsess — GNOME/RDP Session Repair Tool  
*A recovery utility for restoring broken GNOME or RDP desktop sessions*

`repsess` repairs corrupted or partially broken GNOME/RDP sessions by terminating stale processes, clearing authority files, and restarting GNOME shell components.  
It is designed for situations where the graphical environment becomes unstable, incomplete, or fails to load correctly after reconnecting via RDP or after an interrupted logout.

---

## 🎯 Purpose

Modern GNOME sessions can become corrupted when:

- an RDP session disconnects unexpectedly  
- a logout is interrupted or only partially completes  
- stale GNOME/Xorg processes remain running  
- `.Xauthority` or `.ICEauthority` files become invalid  
- GNOME shell fails to restart cleanly  
- UI components (taskbar, systray, desktop icons) fail to load  

`repsess` provides a **safe, predictable, operator‑grade** way to repair the session without requiring a full reboot.

---

# 🧩 When You Should Use repsess

This tool is specifically designed for scenarios such as:

### **1. Partial logout preventing full login**  
You attempt to log in via RDP or locally, but:

- the login screen loops  
- the desktop loads only partially  
- GNOME hangs before showing the UI  
- the session appears “half‑open” from a previous connection  

This is one of the most common GNOME/RDP failure modes.

---

### **2. RDP reconnect causes missing UI elements**  
After reconnecting:

- the taskbar is missing  
- the system tray doesn’t load  
- desktop icons don’t appear  
- GNOME shell is frozen or unresponsive  

`repsess` clears stale processes and restarts GNOME cleanly.

---

### **3. GNOME shell crashes or refuses to reload**  
If you see:

- a blank screen  
- a frozen wallpaper  
- no panels or menus  
- a session that “looks logged in but isn’t usable”  

This tool resets the session components safely.

---

### **4. Authority file corruption**  
If `.Xauthority` or `.ICEauthority` becomes corrupted, you may see:

- “Unable to open display”  
- “Authentication failed”  
- “Cannot start GNOME session”  

`repsess` removes stale authority files so GNOME can regenerate them.

---

# 🛠️ Usage

```
repsess [--dry-run] [--verbose]
```

### Examples
```
repsess
repsess --dry-run
repsess --verbose
```

---

# 🔧 Flags

### **--dry-run**
Shows what would happen **without executing any commands**.

Useful for:

- auditing behaviour  
- verifying safety  
- training new operators  

### **--verbose**
Prints detailed logs of each action.

Useful for:

- debugging  
- understanding the repair sequence  
- confirming which processes were terminated  

---

# ⚙️ What repsess Actually Does

The tool performs a controlled, safe repair sequence:

### **1. Terminates stale GNOME/Xorg processes**
Processes such as:

- `gnome-shell`  
- `gnome-session`  
- `gnome-keyring`  
- `Xorg`  
- `Xwayland`  

These often remain running after a broken logout or RDP disconnect.

---

### **2. Removes stale authority files**
```
~/.Xauthority
~/.ICEauthority
```

These files store session authentication tokens.  
If they become corrupted, GNOME cannot start correctly.

---

### **3. Restarts GNOME shell**
Runs:

```
gnome-shell --replace
```

This reloads the desktop environment without requiring a reboot.

---

# 🧭 Expected Output

A successful repair looks like:

```
[repsess] Repairing GNOME/RDP session…
[repsess] Session repair complete.
If UI elements do not reappear, log out and back in.
```

If verbose mode is enabled, you’ll see each action logged.

---

# 🩺 Troubleshooting

### **UI still missing after running repsess**
Try logging out and back in — GNOME may need a fresh session.

### **Still stuck at login loop**
Check disk space:

```
df -h
```

A full disk can prevent GNOME from creating session files.

### **RDP still loads a blank screen**
Restart the RDP service:

```
sudo systemctl restart xrdp
```

### **Authority files keep corrupting**
This may indicate:

- a failing disk  
- a misconfigured RDP client  
- a GNOME extension causing crashes  

---

# 🔗 Related Tools

| Tool | Purpose |
|------|---------|
| `cleanup` | Clears temp files and system clutter |
| `diag` | Checks system health and environment |
| `update` | Refreshes packages and locate DB |

---

## 🤖 AI & Ethics Disclosure

This tool and its documentation were co‑authored with AI assistance.  
For details on responsible use, transparency, and authorship, see the **AI & Ethics** section in the Toolbox README.

🔙 Return to [Toolbox](https://github.com/Mark-a-Hamilton/Toolbox)
