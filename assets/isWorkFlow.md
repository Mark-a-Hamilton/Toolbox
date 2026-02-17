# 📐 **assets/isWorkflow.md — Injection Scanner Workflow Diagram**


********************
flowchart TD

    A[Start is Engine] --> B[Load Profile<br/>(default: stealth.json)]
    B --> C{Profile Valid?}

    C -- "No" --> Z[Exit with Error]
    C -- "Yes" --> D[Begin Payload Loop]

    D --> E[Send Request<br/>(GET or POST)]
    E --> F[Receive Response]

    F --> G[Iterate Modules<br/>(DBI, XSS, CMDI, etc.)]

    G --> H[Check Signatures<br/>(pattern → meaning)]

    H --> I{Signature Match?}

    I -- "Yes" --> J[Record Finding<br/>(module, payload, meaning)]
    I -- "No" --> D2[Next Module or Payload]

    J --> D2

    D2 -->|More Payloads| D
    D2 -->|No More Payloads| K[Generate Report]

    K --> L{DBI Detected?}

    L -- "No" --> M[Finish Scan]
    L -- "Yes" --> N[Classify DB Type<br/>(SQL or NoSQL)]

    N --> O{--auto-creds Used?}

    O -- "No" --> M
    O -- "Yes" --> P[Run Credential Extraction<br/>(SQL or NoSQL)]

    P --> M[Finish Scan]

********************
```markdown
# Injection Scanner (is) — Engine Workflow Diagram

```mermaid
flowchart TD

    A[Start is Engine] --> B[Load Profile\n(default: stealth.json)]
    B --> C{Profile Valid?}
    C -- No --> Z[Exit with Error]
    C -- Yes --> D[Iterate Payloads]

    D --> E[Send Single Request\n(GET or POST)]
    E --> F[Receive Response]

    F --> G[Iterate Modules\n(DBI, XSS, CMDI, LFI, etc.)]
    G --> H[Check Signatures\n(pattern → meaning)]

    H --> I{Signature Match?}
    I -- Yes --> J[Record Finding\n(module, payload, meaning)]
    I -- No --> D2[Next Module/Payload]

    J --> D2[Next Module/Payload]

    D2 -->|More Payloads| D
    D2 -->|No More Payloads| K[Generate Report]

    K --> L{DBI Detected?}
    L -- No --> M[Finish Scan]
    L -- Yes --> N[Classify DB Type\n(SQL or NoSQL)]

    N --> O{--auto-creds Used?}
    O -- No --> M[Finish Scan]
    O -- Yes --> P[Run Credential Extraction]

    P --> M[Finish Scan]
```

---

# 🧩 What This Diagram Shows

### ✔ **Profile Loading**
The engine loads:

- `profiles/stealth.json` by default  
- or any profile specified with `--profile`  

### ✔ **Payload Loop**
Each payload is sent **once**, regardless of how many modules use it.

### ✔ **Module Loop**
Every module checks the same response for its own signatures.

### ✔ **Signature Matching**
If a signature matches:

- the finding is recorded  
- classification is applied (e.g., SQL vs NoSQL)  

### ✔ **DBI Classification**
If DBI is detected:

- the engine determines SQL or NoSQL  
- this enables optional credential extraction  

### ✔ **Credential Extraction**
Only runs when:

```
--auto-creds
```

is used.

### ✔ **Safe Termination**
The engine never:

- exploits  
- brute‑forces  
- fuzzes  
- modifies state  

It only detects and reports.

---

# 🧭 Why This Asset Matters

This workflow diagram:

- gives newcomers instant clarity  
- shows the engine’s architecture visually  
- reinforces the data‑driven design  
- demonstrates professional engineering discipline  
- makes the repo feel complete and polished  
- helps future maintainers understand the logic without reading code  
- supports your CV and interview narrative  

It’s the kind of asset that turns a tool into a **framework**.

---
