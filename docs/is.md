# 📘 **Injection Scanner (is) — Full Documentation**

## 1. Introduction

`is` (Injection Scanner) is a **data‑driven, low‑noise, defensive reconnaissance engine** designed to detect injection vulnerabilities using:

- **minimal payloads**  
- **minimal requests**  
- **maximum response analysis**  
- **zero exploitation**  

It is built for **system hardening**, not offensive exploitation.

The engine loads **JSON profiles** that define:

- payloads  
- modules  
- signatures  
- classifications  

This makes the scanner:

- dynamic  
- future‑proof  
- easy to extend  
- safe to run  
- ideal for blue‑team hardening  

---

## 2. Core Philosophy

The engine is built on four principles:

### **1. Minimal Payloads**  
Only the smallest, safest payloads are used.

### **2. Minimal Requests**  
Each payload is sent once.  
Multiple modules analyse the same response.

### **3. Maximum Analysis**  
Every module checks every response for signatures.

### **4. Zero Exploitation**  
No brute force.  
No fuzzing.  
No destructive payloads.  
No state‑changing actions.

This makes `is` a **safe, controlled, defensive tool**.

---

## 3. Directory Structure

Your repo now contains only the components that matter:

```
is
├── is                      # The engine
├── profiles/
│   ├── stealth.json        # Default minimal profile
│   └── full.json           # Full-spectrum profile
└── docs/
    └── is.md               # This documentation
```

No legacy scripts.  
No THM leftovers.  
No clutter.

This is a clean, professional structure.

---

## 4. Engine Architecture

The engine is **data‑driven**, meaning:

- The Python code never contains payloads or signatures.
- All detection logic lives in JSON profiles.
- The engine simply:
  1. Loads a profile  
  2. Sends each payload once  
  3. Checks all modules and signatures  
  4. Reports findings  
  5. Optionally runs credential extraction  

### 4.1 Engine Flow

1. Load profile (default: `stealth.json`)  
2. For each payload:
   - Send request  
   - Analyse response  
   - Check all modules  
   - Match signatures  
3. Classify DBI (SQL vs NoSQL)  
4. Report findings  
5. If `--auto-creds` is used:
   - Run SQL or NoSQL credential extraction  

### 4.2 Why this architecture matters

- Payloads evolve → engine stays the same  
- New injection types → engine stays the same  
- New signatures → engine stays the same  
- Client‑specific profiles → engine stays the same  

This is how professional scanners like Nuclei and Nikto work.

---

## 5. Profiles

Profiles define:

- which payloads to send  
- which modules to activate  
- which signatures to check  
- how to classify vulnerabilities  

Profiles live in:

```
profiles/
```

There are only **two generic profiles** that make sense without a specific use‑case:

---

## 5.1 Stealth Profile (default)

`stealth.json` is the default profile used when no profile is specified.

It covers:

- DBI (SQL + NoSQL)  
- XSS  
- CMDI  
- LFI  
- CRLF  
- Open Redirect  

Using only **two payloads**:

- `;`  
- `<script>1</script>`  

This profile is ideal for:

- quick triage  
- low‑noise reconnaissance  
- demonstrating vulnerabilities quietly  
- showing how issues can evade blue‑team detection  

This is the profile that runs when you simply type:

```
is --url http://target
```

---

## 5.2 Full Profile

`full.json` includes:

- everything in stealth.json  
- SSTI  
- LDAP injection  
- XPath injection  
- XXE  
- Prototype pollution  
- GraphQL introspection  
- ReDoS  
- Header injection  
- JSON injection  
- JWT injection  
- Deserialization signatures  
- Framework‑specific signatures  

Still minimal payloads.  
Still minimal requests.  
Maximum coverage.

This is the profile you use for full assessments:

```
is --url http://target --profile full.json
```

---

## 6. How to Expand Profiles

Profiles are designed to be **easy to modify**, even for newcomers.

### 6.1 Adding a new injection type

Add a new module under an existing payload:

```json
"LDAP": [
  ["LDAPException", "LDAP Injection"],
  ["Invalid DN", "LDAP Injection"]
]
```

### 6.2 Adding new signatures

Append to the module:

```json
["new error message", "Meaning of the signature"]
```

### 6.3 Adding a new payload

Add a new entry to `"payloads"`:

```json
{
  "payload": "{{7*7}}",
  "modules": {
    "SSTI": [
      ["49", "SSTI arithmetic evaluation"]
    ]
  }
}
```

### 6.4 No engine changes required

The engine automatically:

- loads  
- validates  
- executes  
- classifies  
- reports  

…without modification.

---

## 7. Regenerating Profiles with AI (Future‑Proofing)

If the JSON files haven’t been updated for a year or more, a newcomer can regenerate them easily.

### 7.1 Regenerating stealth.json

Ask an AI:

> “Generate a minimal‑payload, minimal‑request injection detection profile for my data‑driven engine.  
> Include DBI, XSS, CMDI, LFI, CRLF, and Open Redirect.  
> Use only 1–2 payloads.  
> Output in the JSON structure:  
> {name, description, payloads[payload, modules[module_name[pattern, meaning]]]}”

### 7.2 Regenerating full.json

Ask an AI:

> “Generate a full-spectrum injection detection profile for my data‑driven engine.  
> Use minimal payloads but include all major injection classes:  
> DBI, XSS, CMDI, LFI, CRLF, Redirect, SSTI, LDAP, XPath, XXE, Prototype Pollution, GraphQL, ReDoS, Header Injection, JSON Injection, JWT Injection, Deserialization, Framework-specific signatures.  
> Output in the JSON structure:  
> {name, description, payloads[payload, modules[module_name[pattern, meaning]]]}”

### 7.3 Why this works

Because the engine is **data‑driven**, not code‑driven.

As long as the JSON structure is respected, the engine will:

- ingest  
- validate  
- execute  
- classify  
- report  

…without modification.

This makes the tool **future‑proof**.

---

## 8. Credential Extraction Modules

Credential extraction is optional and only runs when requested.

### 8.1 SQL Credential Extraction

Triggered when:

```
--auto-creds
```

and DBI is classified as SQL.

Uses:

- `' OR LENGTH(username)=X --`  
- `' OR LENGTH(password)=X --`  

### 8.2 NoSQL Credential Extraction

Triggered when:

```
--auto-creds
```

and DBI is classified as NoSQL.

Uses:

- `{"$ne": [...]}`  
- `{"password": {"$ne": [...]}}`  

### 8.3 Credential extraction only

```
is --url <target> --creds-only --db-type sql
```

---

## 9. Usage Examples

### Stealth scan (default)

```
is --url http://target/page?id=1
```

### Full scan

```
is --url http://target/page?id=1 --profile full.json
```

### Auto credential extraction

```
is --url http://target/login --auto-creds
```

### Credential extraction only

```
is --url http://target/login --creds-only --db-type nosql
```

---

## 10. Maintenance Guidance

### 10.1 When to update profiles

- New injection techniques discovered  
- New frameworks become common  
- New error signatures appear  
- A client has specific requirements  
- Once per year as a routine update  

### 10.2 How to update profiles

- Edit JSON directly  
- Or regenerate using AI prompts  
- No engine changes required  

### 10.3 How to test changes

```
is --url http://test --profile <modified.json> --verbose
```

---

## 11. Summary

`is` is a:

- dynamic  
- data‑driven  
- low‑noise  
- safe  
- future‑proof  
- defensive reconnaissance engine  

It answers the question:

> “Is this site vulnerable to injection attacks?”

…without causing harm, and without requiring code changes as attack methods evolve.

---



