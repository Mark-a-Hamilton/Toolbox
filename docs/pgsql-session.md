# 🐘 pgsql-session — Session‑Bound PostgreSQL Wrapper  
*A controlled, on‑demand PostgreSQL instance for temporary or minimal environments*

`pgsql-session` starts a dedicated PostgreSQL service instance for the duration of a single `psql` session.  
When the user exits `psql`, the service is automatically stopped.  
This ensures PostgreSQL only runs when required, reducing resource usage and preventing unnecessary background services.

This behaviour is ideal for minimal systems, lab VMs, DFIR workflows, or environments where PostgreSQL is not intended to run persistently.

---

## 🎯 Purpose

Some environments do **not** require PostgreSQL to run continuously.  
Examples include:

- minimal Kali installations  
- DFIR triage VMs  
- lab environments  
- systems where PostgreSQL is used only occasionally  
- machines where PostgreSQL should not remain active for security reasons  

`pgsql-session` provides a **safe, predictable, session‑scoped** way to use PostgreSQL without enabling or running the service permanently.

---

# 🧩 When You Should Use pgsql-session

### **1. You only need PostgreSQL temporarily**
If you’re running a one‑off query, testing a database, or performing a short task, this tool ensures PostgreSQL runs only for the duration of your session.

---

### **2. You want to avoid PostgreSQL running in the background**
Some operators prefer to keep services disabled unless actively needed.  
`pgsql-session` enforces that discipline automatically.

---

### **3. You’re working in a DFIR or lab VM**
In forensic or lab environments, persistent services can:

- consume unnecessary resources  
- introduce noise  
- create unwanted logs  
- complicate evidence handling  

A session‑bound database avoids these issues.

---

### **4. PostgreSQL is installed but disabled by default**
This is common in:

- minimal distros  
- hardened systems  
- custom VM images  

`pgsql-session` provides on‑demand activation without enabling the service globally.

---

# 🛠️ Usage

```
pgsql-session [psql arguments]
```

### Examples
```
pgsql-session
pgsql-session -d mydatabase
pgsql-session -U analyst -h localhost
```

Any arguments passed to `pgsql-session` are forwarded directly to `psql`.

---

# ⚙️ What pgsql-session Actually Does

The tool performs a clean, controlled sequence:

### **1. Starts a PostgreSQL instance**
```
sudo systemctl start postgresql@18-main.service
```

This uses a **systemd instance unit**, allowing multiple clusters or versions to coexist.

---

### **2. Launches psql in the foreground**
```
psql "$@"
```

`psql` blocks until the user exits.

---

### **3. Stops PostgreSQL when the session ends**
```
sudo systemctl stop postgresql@18-main.service
```

This ensures PostgreSQL is not left running unintentionally.

---

# 🧭 Expected Output

### **Starting the session**
```
[pgsql-session] Starting PostgreSQL service for this session…
[pgsql-session] Launching psql…
```

### **After exiting psql**
```
[pgsql-session] psql exited — stopping PostgreSQL service…
[pgsql-session] PostgreSQL session complete.
```

---

# 🩺 Troubleshooting

### **PostgreSQL fails to start**
Check logs:

```
sudo journalctl -u postgresql@18-main.service
```

### **Cluster version mismatch**
Ensure the service name matches your installed cluster:

```
ls /etc/systemd/system/postgresql@*.service
```

### **psql not found**
Install the client:

```
sudo apt install postgresql-client
```

### **Service stops immediately**
This may indicate:

- missing cluster  
- corrupted data directory  
- incorrect PostgreSQL version  

---

# 🔗 Related Tools

| Tool | Purpose |
|------|---------|
| `pgsql-state` | Ensures PostgreSQL is running persistently |
| `diag` | System diagnostics and environment checks |
| `cleanup` | System hygiene and temporary file cleanup |
| `update` | Package updates and locate DB refresh |

---

## 🤖 AI & Ethics Disclosure

This tool and its documentation were co‑authored with AI assistance.  
For details on responsible use, transparency, and authorship, see the **AI & Ethics** section in the Toolbox README.

🔙 Return to [Toolbox](https://github.com/Mark-a-Hamilton/Toolbox)

- or a **combined PostgreSQL tools index**  

Just tell me which direction you want to take.
