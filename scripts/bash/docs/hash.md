# 🔐 hash — MD5 Hash Creation & Verification Tool  
*A minimal, predictable, operator‑grade utility for generating and verifying MD5 hash files*

`hash` is a lightweight tool for creating MD5 hash files and verifying the integrity of disk images, evidence files, or any binary data.  
It provides two clear modes:

- **Mode 1:** Generate a hash file  
- **Mode 2:** Verify an image against an existing hash file  

This document explains exactly how the tool works, when to use each mode, and how to avoid common mistakes.

---

# 🎯 Purpose

Hashing is a fundamental part of:

- digital forensics  
- evidence handling  
- integrity verification  
- file transfer validation  
- backup verification  
- malware analysis  
- DFIR workflows  

This tool provides a **simple, predictable, no‑nonsense** way to:

- generate a hash file for an image  
- verify an image against a known hash  
- ensure integrity after transfer or storage  
- detect tampering or corruption  

It is intentionally minimal and operator‑friendly.

---

# 🛠️ Usage

```
hash <image_filename> [hash_filename]
```

### Examples

#### **Generate a hash file**
```
hash disk.img
```
Creates:
```
disk.img.md5
```

#### **Verify an image against an existing hash**
```
hash disk.img disk.img.md5
```

---

# 🧩 How the Tool Works

The tool operates in **two mutually exclusive modes** depending on whether a second argument is provided.

---

## **Mode 1 — Create a Hash File**

Triggered when **only the image filename is supplied**:

```
hash disk.img
```

The tool will:

1. Validate that `disk.img` exists  
2. Generate an MD5 hash  
3. Save it to `disk.img.md5`  
4. Set the file to read‑only (`chmod 444`)  

### Output example
```
[hash] Generating MD5 hash for 'disk.img'...
[hash] Hash saved to 'disk.img.md5'
```

This mode is ideal for:

- creating baseline hashes  
- preparing evidence for transfer  
- documenting acquisition integrity  
- generating hashes for chain‑of‑custody  

---

## **Mode 2 — Verify Against an Existing Hash File**

Triggered when **both an image and a hash file are supplied**:

```
hash disk.img disk.img.md5
```

The tool will:

1. Validate both files exist  
2. Generate a temporary hash using `mktemp`  
3. Display both hashes  
4. Compare them using `cmp`  
5. Report whether they match  

### Output example
```
[hash] Verifying 'disk.img' against 'disk.img.md5'...

Source hash file:
<contents>

Current image hash:
<contents>

[hash] Comparing hashes...
✅ Hashes match — image integrity verified.
```

If the hashes differ:

```
⚠️ Hash mismatch — image may be altered or corrupted.
```

This mode is ideal for:

- verifying evidence after transfer  
- checking integrity after storage  
- confirming no tampering occurred  
- validating backups or forensic images  

---

# 🧭 Expected Behaviour

### ✔ If the image file does not exist
```
[hash] Error: Image file 'disk.img' not found.
```

### ✔ If the hash file does not exist (Mode 2)
```
[hash] Error: Hash file 'disk.img.md5' not found.
```

### ✔ If the hash matches
```
✅ Hashes match — image integrity verified.
```

### ✔ If the hash does not match
```
⚠️ Hash mismatch — image may be altered or corrupted.
```

---

# 🩺 Troubleshooting

### **The hash file has different formatting**
Ensure the hash file was generated using `md5sum` or this tool.  
Other tools may include additional metadata.

### **The hash file is empty**
This usually indicates:

- a failed acquisition  
- a truncated file  
- a permissions issue  

### **The image hash changes unexpectedly**
Possible causes:

- corruption  
- tampering  
- incomplete transfer  
- filesystem issues  
- compression or decompression errors  

### **Permission denied**
Ensure the image is readable:

```
sudo chmod +r disk.img
```

---

# 🔗 Related Tools

| Tool | Purpose |
|------|---------|
| `xfer` | Remote transfer + execution utility |
| `cleanup` | System hygiene and temporary file cleanup |
| `diag` | System diagnostics and environment checks |
| `mda4w` | Windows memory dump analysis |
| `pgsql-state` | Ensure PostgreSQL is running |
| `pgsql-session` | Session-bound PostgreSQL instance |

---

## 🤖 AI & Ethics Disclosure

This tool and its documentation were co‑authored with AI assistance.  
For details on responsible use, transparency, and authorship, see the **AI & Ethics** section in the Toolbox README.


🔙 Return to [Toolbox](https://github.com/Mark-a-Hamilton/Toolbox)
