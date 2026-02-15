# 🧰 tool-box

`tool-box` is the central indexer for the Toolbox suite.  
It lists all available tools across supported languages and extracts each tool’s metadata (Script Purpose + Version) directly from its embedded header. When provided a tool name, it displays the detailed help block for Bash tools.

---

## 🎯 Purpose

`tool-box` provides a unified, operator‑friendly way to:

- enumerate all installed tools across Bash, Python, and PHP  
- extract Script Purpose and Version from each tool’s metadata block  
- display detailed help for any Bash tool  
- support quick discovery and navigation within the Toolbox  

It acts as the **entry point** for understanding what the Toolbox contains and how each tool behaves.

---

## 🧪 Usage

### List All Tools
```bash
tool-box
```
Displays all tools grouped by language, including their purpose and version.

### Show Help for a Specific Bash Tool
```bash
tool-box diag
```
Extracts and prints the tool’s embedded help block.

### Python & PHP Tools
These tools use their own built‑in help flags:
```bash
<tool-name> -h
```

---

## 🧩 Embedded Features

| Feature         | Description                                                  |
|----------------|--------------------------------------------------------------|
| Metadata Scan  | Reads Script Purpose + Version from each tool’s header       |
| Multi‑Language | Indexes Bash, Python, and PHP tools                          |
| Help Extraction| Displays Bash help blocks via `tool-box <tool>`              |
| Auto‑Discovery | Scans `/usr/local/bin/<lang>` for installed tools            |
| Versioning     | Fully compatible with Toolbox’s `YYYY.MM.DD‑BUILD` model     |

---

## 📂 Directory Structure

`tool-box` expects tools to be organised as:

```
/usr/local/bin/
    bash/
    python/
    php/
```

Each tool must include a metadata block at the top of the script:

```
# Script Purpose : <description>
# Version        : <version>
```

This allows `tool-box` to index the tool automatically.

---

## 📁 Output

### When listing all tools:
- Language groupings  
- Tool names  
- Script Purpose  
- Version (extracted from metadata)

### When showing a specific tool:
- Full help block (Bash tools only)  
- Cleanly formatted output for readability  

---

## 🤖 AI Integration

`tool-box` was refined using AI‑assisted development to ensure:

- consistent metadata parsing  
- predictable output formatting  
- alignment with the Toolbox architecture  
- operator‑grade clarity  

The tool remains fully transparent and human‑auditable.

---

## 🧭 Contributor Guidance

- Ensure every tool includes a metadata block with Script Purpose + Version  
- Follow the Toolbox versioning model: `YYYY.MM.DD‑BUILD`  
- Keep help blocks clean and structured  
- Avoid hardcoded paths outside `/usr/local/bin/<lang>`  
- Validate changes by running:
  ```bash
  tool-box
  tool-box <tool-name>
  ```

---

## 🤖 AI & Ethics Disclosure  

This tool was co‑authored with AI assistance.  
For details on ethical integration and responsible authorship, see:  
ethics_AI.md (github.com in Bing) [(bing.com in Bing)](https://www.bing.com/search?q="https%3A%2F%2Fwww.bing.com%2Fsearch%3Fq%3D%2522https%253A%252F%252Fgithub.com%252FMark-a-Hamilton%252FMark-a-Hamilton.github.io%252Fblob%252Fmain%252Fethics_AI.md%2522")

🔙Return to [Toolbox](https://github.com/Mark-a-Hamilton/Toolbox)
