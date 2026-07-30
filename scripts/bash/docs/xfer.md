# 🛰️ xfer — Remote Transfer & Execution Utility  
*A predictable, operator‑grade wrapper for SCP + SSH workflows*

`xfer` provides a clean, disciplined interface for remote file transfer, remote command execution, and trigger‑file verification.  
It wraps standard `scp` and `ssh` behaviour into a consistent, auditable tool that behaves the same way every time.

This tool is ideal for operators who need a **simple, reliable, repeatable** way to:

- pull files from a remote host  
- push files to a remote host  
- execute commands or scripts remotely  
- verify completion via trigger files  

---

# 📖 Overview

`xfer` supports four subcommands:

| Subcommand | Purpose |
|-----------|---------|
| `get`     | Pull a file or directory from remote → local |
| `put`     | Push a file or directory from local → remote |
| `run`     | Execute a remote command or script |
| `test`    | Count `.trg` trigger files in a remote directory |

All operations use standard SSH/SCP under the hood, with predictable behaviour and clear error codes.

---

# 🧩 Usage

```
xfer get  IP USER REMOTE_PATH [LOCAL_DEST] [FLAGS]
xfer put  IP USER LOCAL_PATH  REMOTE_DEST [FLAGS]
xfer run  IP USER REMOTE_COMMAND
xfer test IP USER REMOTE_PATH EXPECTED_COUNT
```

---

# 🛠️ Subcommands in Detail

---

## 1. 📥 GET — Pull from Remote to Local

### **Syntax**
```
xfer get IP USER REMOTE_PATH [LOCAL_DEST] [FLAGS]
```

### **Defaults**
- If `LOCAL_DEST` is omitted → defaults to `~/Downloads`
- `FLAGS` are passed directly to `scp` (e.g., `-r` for recursive)

### **Example**
```
xfer get 10.10.10.10 mark /etc/passwd ~/Downloads
```

### **Notes**
- Wildcards **must** be quoted:
  ```
  xfer get 10.10.10.10 mark '/var/log/*.log'
  ```
- SCP flags behave exactly as they do in native scp.

---

## 2. 📤 PUT — Push from Local to Remote

### **Syntax**
```
xfer put IP USER LOCAL_PATH REMOTE_DEST [FLAGS]
```

### **Example**
```
xfer put 10.10.10.10 mark ./payload.sh /tmp '-r'
```

### **Important Wildcard Rules**
- **Local paths must NOT be quoted**  
  (SCP needs to expand them locally)
- **Remote paths MUST be quoted**  
  (to avoid shell expansion on your machine)

### **Examples**
Correct:
```
xfer put 10.10.10.10 mark LinSuite.* '/tmp/'
```

Incorrect:
```
xfer put 10.10.10.10 mark 'LinSuite.*' /tmp/
```

---

## 3. 🏃 RUN — Execute a Remote Command or Script

### **Syntax**
```
xfer run IP USER REMOTE_COMMAND
```

### **Examples**
Run a command:
```
xfer run 10.10.10.10 mark 'uname -a'
```

Run a script:
```
xfer run 10.10.10.10 mark /tmp/payload.sh
```

### **Behaviour**
- If the remote command is an **absolute path**, `xfer` will:
  - `chmod +x` the file (silently)
  - execute it directly
- If it’s not an absolute path, it is executed as‑is.

### **Exit Codes**
`xfer run` returns the **remote command’s exit code**.

This makes it ideal for automation.

---

## 4. 🧪 TEST — Trigger File Verification

Used to confirm whether a remote process has completed.

### **Syntax**
```
xfer test IP USER REMOTE_DIR EXPECTED_COUNT
```

### **Example**
```
xfer test 10.10.10.10 mark /tmp/triggers 2
```

### **Behaviour**
- Normalises directory path  
- Counts `*.trg` files remotely  
- Returns a meaningful exit code:

| Exit Code | Meaning |
|-----------|---------|
| `0` | Expected number of trigger files found |
| `1` | Some triggers found, but fewer than expected |
| `2` | No trigger files found |
| `3` | SSH failure |

This makes it ideal for polling loops or automation pipelines.

---

# 🔐 Authentication Behaviour

`xfer` uses SSH with:

- password  
- keyboard‑interactive  
- **public key authentication disabled**  
- host key checking disabled  

This ensures predictable behaviour in:

- fresh VMs  
- lab environments  
- ephemeral hosts  
- automation pipelines  

---

# 🧭 Practical Examples

### **Pull a directory recursively**
```
xfer get 192.168.1.50 mark '/var/log/nginx/' ~/logs '-r'
```

### **Push a script and run it**
```
xfer put 192.168.1.50 mark ./scan.sh /tmp
xfer run 192.168.1.50 mark /tmp/scan.sh
```

### **Check for completion triggers**
```
xfer test 192.168.1.50 mark /tmp/triggers 3
if [[ $? -eq 0 ]]; then
    echo "All tasks complete."
fi
```

---

# 🧱 Error Handling

`xfer` uses `set -euo pipefail`, meaning:

- missing variables → error  
- failed commands → error  
- pipeline failures → error  

This ensures predictable, operator‑grade behaviour.

---

# 🧠 Design Philosophy

`xfer` exists to:

- remove ambiguity from SCP/SSH usage  
- provide predictable behaviour across environments  
- simplify remote operations  
- support automation and scripting  
- enforce consistent quoting and wildcard rules  

It is intentionally minimal and transparent.

---

# 🤖 AI & Ethics Disclosure

This tool and documentation were co‑authored with AI assistance.  
For details on responsible use, transparency, and authorship, see the **AI & Ethics** section in the Toolbox README.
