# tool-launch-desktop

## 🧰 Purpose
Launches a Linux desktop session with X11 rendering, D-Bus setup, ICE socket fix, and session lock cleanup. Designed for local use in authorized environments. Logs all actions for traceability.

## 🧑‍💻 Author
Mark Hamilton │ Co-Pilot AI assisted

## 📦 Package
toolbox

## 🛡️ Ethical Scope
This tool is non-intrusive and intended for local use only. It does not initiate remote connections or modify external systems. See `ethics_AI.md` for usage boundaries.

## ⚙️ Usage
```bash
tool-ldp
```

## 📂 Output Files
- `~/Documents/desktop-launch.log`: Full session log

## 🔧 Actions Performed
- Resolves `DISPLAY` via default gateway
- Sets X11 rendering variables (`LIBGL`, `GDK_BACKEND`, `QT_QPA_PLATFORM`)
- Starts D-Bus session if missing
- Fixes ICE socket ownership and permissions
- Clears stale XFCE session locks
- Starts `xfwm4` if not running
- Launches full XFCE session via `startxfce4`

## 🔗 Related Tools
- `tool-lstnr`: Ethical listener with traceability
- `tool-box`: Index and help parser
- `tool-diag`: Diagnostic wrapper

## 🧠 Contributor Notes
This script is modular, traceable, and aligned with toolbox standards. Metadata block is compatible with `tool-box` indexing. Designed for authorized desktop session recovery or launch.
