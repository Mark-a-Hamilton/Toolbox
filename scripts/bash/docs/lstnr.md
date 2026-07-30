# 🎧 lstnr

`lstnr` is an ethical, operator‑grade listener tool within the Toolbox suite.  
It binds to a specified port using **socat** (preferred) or **netcat** (fallback), automatically selecting the VPN IP if available. The tool supports dry‑run simulation, logging, and hash‑based traceability.

---

## 🎯 Purpose

`lstnr` provides a safe, controlled way to:

- Start a listener on a chosen port  
- Prefer **socat** for stable PTY‑backed shells  
- Fall back to **netcat** when socat is unavailable  
- Automatically detect VPN IP (tun0) or default route IP  
- Log session output for auditing  
- Generate SHA‑256 hashes for traceability  

It is designed for **authorized, defensive, and training environments only**.

---

## ⚠️ Dependencies

`lstnr` requires at least one of the following tools to be installed:

| Dependency | Purpose |
|-----------|---------|
| **socat** | Preferred listener with PTY support |
| **netcat** (`nc`) | Fallback listener if socat is unavailable |

If neither is installed, the listener cannot start.

Install on Debian/Ubuntu/Kali:

```bash
sudo apt install socat netcat-openbsd
```

---

## 🧪 Usage

```bash
lstnr [--port <PORT>] [--dry-run] [--log] [--hashmap]
```

### Examples

```bash
lstnr
lstnr --port 5555 --log --hashmap
lstnr --dry-run
```

---

## 🧩 Flags

| Flag        | Description                                      |
|-------------|--------------------------------------------------|
| `--port`    | Specify listener port (default: 4444)            |
| `--dry-run` | Show configuration without launching listener    |
| `--log`     | Log session output to `~/Documents/listener.log` |
| `--hashmap` | Generate `.hashmap` audit files                  |

---

## 📂 Output Files

| File Path                                | Purpose                          |
|-------------------------------------------|----------------------------------|
| `~/Documents/listener.log`                | Session log (if `--log` used)    |
| `~/Documents/.hashmap/lstnr.hash`         | SHA‑256 hash of the script       |
| `~/Documents/.hashmap/lstnr.timestamp`    | Timestamp of listener start      |

All output locations are displayed during execution.

---

## 🛡️ Ethical Scope

This tool is **passive and non‑exploitative**.  
It does **not** initiate outbound connections, deliver payloads, or perform offensive actions.

It is intended exclusively for:

- authorized environments  
- defensive training  
- controlled testing  
- blue‑team workflows  

Misuse outside permitted environments is strictly prohibited.

---

## 🧠 Contributor Notes

- `lstnr` replaces legacy ad‑hoc netcat/socat scripts  
- Metadata block is compatible with `tool-box` indexing  
- Logging and hashmap features follow Toolbox standards  
- The tool is modular and easy to extend (e.g., UDP mode, TLS socat mode)

---

## 🤖 AI & Ethics Disclosure

This tool and its documentation were co‑authored with AI assistance.  
For details on responsible use, transparency, and authorship, see the **AI & Ethics** section in the Toolbox README.

🔙 Return to [Toolbox](https://github.com/Mark-a-Hamilton/Toolbox)
