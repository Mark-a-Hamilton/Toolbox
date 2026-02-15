# 🖥️ Kali Environment Creation Workflow  
*A visual guide to building a clean, complete Kali installation using the Toolbox ecosystem*

This workflow provides a **visual, high‑level map** of the entire process for creating a Kali environment on Windows (Hyper‑V or WSL), installing the Toolbox, and completing a full Kali installation using the `fki` tool.

It is the first asset in the Toolbox visual library and serves as the entry point for new users.

---

## 📊 Workflow Diagram (Mermaid)

GitHub renders Mermaid diagrams natively.  
This flowchart shows the complete environment‑creation process at a glance.

```mermaid
flowchart TD

    A[Start: Windows Host] --> B['Create VM\n(Hyper-V or WSL')]
    B --> C[Install Kali Minimal ISO]
    C --> D[Boot into Kali]
    D --> E[Copy Toolbox Tools<br>to /usr/local/bin/bash/python/php]
    E --> F[Add Toolbox Paths<br>to ~/.bashrc]
    F --> G[Run update Tool]
    G --> H[Run fki Tool<br>(Full Kali Install)]
    H --> I[Run update Again]
    I --> J[Full Kali Environment Ready]
```

---

## 🧭 Step‑By‑Step Explanation

This workflow is designed to be simple, predictable, and beginner‑friendly.

### **1. Create a VM (Hyper‑V or WSL)**  
Follow the instructions in:  
📄 `docs/VirtualMachine.md`

Choose either:

- **Hyper‑V** for a full desktop VM  
- **WSL** for a lightweight CLI environment  

---

### **2. Install the Kali Minimal ISO**  
Use the official minimal installer to create a clean, lightweight base system.

---

### **3. Boot into Kali**  
Log in with the user you created during installation.

---

### **4. Copy Toolbox Tools**  
Create the Toolbox directories:

```bash
sudo mkdir -p /usr/local/bin/bash
sudo mkdir -p /usr/local/bin/python
sudo mkdir -p /usr/local/bin/php
```

Copy your tools into the appropriate folders.

---

### **5. Add Toolbox Paths to `.bashrc`**

```bash
export PATH="/usr/local/bin/bash:/usr/local/bin/python:/usr/local/bin/php:$PATH"
```

Reload:

```bash
source ~/.bashrc
```

---

### **6. Run the update tool**

```bash
sudo update
```

This prepares the system for the full installation.

---

### **7. Run the Full Kali Installer (`fki`)**

```bash
sudo fki
```

This installs the recommended **kali‑linux‑large** meta‑package.

See:  
📄 `docs/fki.md`

---

### **8. Run update again**

```bash
sudo update
```

This final refresh ensures all packages are current.

---

## 🎉 Result

You now have a:

- fully functional  
- reproducible  
- VM‑friendly  
- operator‑grade  

**Kali Linux environment**, built using a clean, deliberate workflow.

---

## 🔗 Related Documentation

| Document | Purpose |
|---------|---------|
| `docs/VirtualMachine.md` | Create the VM environment (Hyper‑V or WSL) |
| `docs/fki.md` | Full Kali installation using `kali-linux-large` |
| `docs/update.md` | System update and locate DB refresh |
| `README.md` | Toolbox overview, ethics, and installation paths |

