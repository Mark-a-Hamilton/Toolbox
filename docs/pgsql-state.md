# 🐘 pgsql-state — PostgreSQL Service State Checker  
*A lightweight utility to ensure PostgreSQL is running before dependent operations continue*

`pgsql-state` is a simple, reliable tool that checks whether the PostgreSQL service is active.  
If the service is not running, the tool starts it and waits briefly to ensure it becomes ready.  
This is especially useful in workflows where PostgreSQL is a prerequisite for scripts, automation, or DFIR tooling.

---

## 🎯 Purpose

Many tools and workflows depend on PostgreSQL being available.  
However, PostgreSQL may not always be running due to:

- system reboots  
- service crashes  
- misconfigured startup behaviour  
- dependency failures  
- manual shutdowns  
- VM suspends/resumes  
- WSL or Hyper‑V session resets  

`pgsql-state` ensures the database is active before continuing, preventing confusing failures later in the workflow.

---

# 🧩 When You Should Use pgsql-state

This tool is ideal in scenarios such as:

### **1. A script requires PostgreSQL but fails with connection errors**
Symptoms include:

- “could not connect to server”  
- “connection refused”  
- “no such file or directory: /var/run/postgresql/.s.PGSQL.5432”  

Running `pgsql-state` ensures the service is up before retrying.

---

### **2. PostgreSQL is disabled or not set to start automatically**
Some environments (especially minimal Kali installs) do not auto‑start PostgreSQL.

`pgsql-state` handles this gracefully.

---

### **3. After a reboot or VM suspend/resume**
PostgreSQL may not restart automatically depending on system configuration.

---

### **4. During DFIR or automation workflows**
If a forensic or automation tool relies on PostgreSQL (e.g., for logging, evidence indexing, or temporary storage), `pgsql-state` ensures the environment is ready.

---

### **5. When using tools that silently assume PostgreSQL is running**
This prevents confusing downstream errors by validating the service state early.

---

# 🛠️ Usage

```
pgsql-state
```

### Example
```
pgsql-state
```

There are no flags — the tool is intentionally minimal.

---

# ⚙️ What pgsql-state Actually Does

The tool performs a simple, predictable sequence:

### **1. Checks whether PostgreSQL is active**
```
systemctl is-active --quiet postgresql
```

### **2. If inactive, starts the service**
```
sudo systemctl start postgresql
```

### **3. Waits briefly to ensure readiness**
A short `sleep` ensures the service is fully initialised.

### **4. Reports the final state**
Clear, operator‑friendly output:

- `[pgsql-state] PostgreSQL is already running.`  
- `[pgsql-state] PostgreSQL is not running — starting service…`  
- `[pgsql-state] PostgreSQL service started.`  

---

# 🧭 Expected Output

### **If PostgreSQL is running**
```
[pgsql-state] Checking PostgreSQL service state…
[pgsql-state] PostgreSQL is already running.
```

### **If PostgreSQL is not running**
```
[pgsql-state] Checking PostgreSQL service state…
[pgsql-state] PostgreSQL is not running — starting service…
[pgsql-state] PostgreSQL service started.
```

---

# 🩺 Troubleshooting

### **PostgreSQL fails to start**
Check service logs:

```
sudo journalctl -u postgresql
```

### **Port already in use**
Another process may be occupying port 5432:

```
sudo lsof -i :5432
```

### **Database cluster not initialised**
Run:

```
sudo pg_createcluster 16 main --start
```

(Version may vary depending on your system.)

### **Systemd not available (WSL1 or minimal environments)**
PostgreSQL may need to be started manually:

```
sudo service postgresql start
```

---

# 🔗 Related Tools

| Tool | Purpose |
|------|---------|
| `diag` | System diagnostics and environment checks |
| `cleanup` | System hygiene and temporary file cleanup |
| `update` | Package updates and locate DB refresh |

---

## 🤖 AI & Ethics Disclosure

This tool and its documentation were co‑authored with AI assistance.  
For details on responsible use, transparency, and authorship, see the **AI & Ethics** section in the Toolbox README.

🔙 Return to [Toolbox](https://github.com/Mark-a-Hamilton/Toolbox)

