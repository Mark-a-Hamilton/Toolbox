# 📘 **sql-creds.py — Blind SQL Credential Extraction Demonstrator**

## 1. Introduction

`sql-creds.py` is a Toolbox module designed to demonstrate how **blind SQL injection** can be used to enumerate usernames and extract passwords from vulnerable endpoints in controlled environments.

It performs:

- blind username enumeration using `LENGTH()`‑based payloads  
- blind password extraction using incremental length probing  
- realistic probing using randomised user‑agents  
- timing jitter to simulate stealthy attacker behaviour  
- optional dry‑run simulation  
- optional logging + hashmap traceability  

This tool is ideal for:

- Windows PrivEsc Arena  
- THM SQL exploitation rooms  
- attacker‑workflow demonstrations  
- defensive detection and forensic reasoning  
- teaching how SQL injection leaks structured data  

It is **non‑malicious**, **non‑destructive**, and intended for **educational use only**.

---

## 2. What This Tool Demonstrates

`sql-creds.py` models the **attacker enumeration → exploitation → credential extraction workflow**, showing:

- how blind SQL injection reveals usernames  
- how incremental length‑based probing leaks passwords  
- how attackers simulate stealth using jitter + user‑agent rotation  
- how defenders can recognise probing patterns  

It reinforces both **attacker literacy** and **defender intuition**.

---

## 3. High‑Level Workflow

```mermaid
flowchart TD
A["Send LENGTH() Payload"] --> B["Enumerate Usernames"]
B --> C["Send LENGTH() Password Payload"]
C --> D["Extract Passwords"]
D --> E["Output Credentials"]
E --> F["Write Logs & Hashmap (optional)"]
```

---

## 4. Usage

### Full enumeration

```
sql-creds.py --url http://target/login
```

### Extract password for a specific user

```
sql-creds.py --url http://target/login --username admin
```

### Dry‑run (simulate without sending requests)

```
sql-creds.py --url http://target/login --dry-run
```

### Verbose mode

```
sql-creds.py --url http://target/login --verbose
```

### Logging + Hashmap traceability

```
sql-creds.py --url http://target/login --log --hashmap
```

---

## 5. Output Files

When optional flags are used:

| File | Purpose |
|------|---------|
| `/var/log/sql-creds.py.log` | Execution log (when `--log` is used) |
| `.hashmap/sql-creds.py.hash` | SHA‑256 hash of the script (when `--hashmap` is used) |
| `.hashmap/sql-creds.py.timestamp` | Timestamp of execution (when `--hashmap` is used) |

These reinforce **traceability**, **repeatability**, and **forensic analysis** — consistent across all Toolbox Python tools.

---

## 6. Blind SQL Username Enumeration

The tool uses payloads like:

```
' OR LENGTH(username)=<n> --
```

If the server responds with:

```
Invalid password: <username>
```

Then the username is discovered.

Example output:

```
[+] Found username: admin
```

This demonstrates how **length‑based probing** can leak structured data.

---

## 7. Blind SQL Password Extraction

Passwords are extracted using:

```
' OR LENGTH(password)=<n> --
```

Each discovered password is printed:

```
[+] Found password for admin: pass123
```

This models how attackers incrementally enumerate secrets using blind‑injection logic.

---

## 8. Example Output

```
[+] Found username: admin
[+] Found password for admin: hunter2

Discovered Credentials:
- admin: hunter2
```

---

## 9. Educational Value

`sql-creds.py` is ideal for:

- demonstrating blind SQL injection  
- teaching length‑based enumeration  
- showing how structured data leaks through error‑based responses  
- modelling attacker workflows for defender training  
- THM rooms involving SQL exploitation  
- internal awareness training  

It is **not** intended for real‑world offensive use.

---

## 10. Limitations

- Assumes the target returns `"Invalid password"` on failed login  
- Only supports JSON POST endpoints  
- No CAPTCHA, rate‑limit, or lockout handling  
- Blind‑injection logic is simplified for teaching  
- Intended for **controlled environments** only  

These limitations are intentional — the tool focuses on **education**, not exploitation.

---

## 11. Summary

`sql-creds.py` is a structured, educational SQL injection demonstrator that:

- performs blind username enumeration  
- extracts passwords using `LENGTH()`‑based payloads  
- models attacker workflows  
- reinforces defensive detection and forensic reasoning  
- integrates cleanly with the Toolbox architecture  

It is transparent, predictable, and ideal for PrivEsc Arena and THM‑style learning.

---

## 📢 Disclaimer

This tool performs **non‑destructive, educational demonstrations only**.  
It does **not** bypass security controls or perform offensive actions.  
Use responsibly and only in environments where you have explicit permission.

---

## 🤖 AI & Ethics Disclosure

This documentation was co‑authored with AI assistance.  
For details on responsible use, transparency, and authorship, see the **AI & Ethics** section in the Toolbox README.

🔙 Return to Toolbox

---
