# 🧰 template

`template` is the foundational scaffold for all future tools in the **Toolbox**.  
It provides a clean, modular, and fully standardised starting point that ensures every new tool integrates seamlessly with the Toolbox architecture, metadata indexing, and operator‑grade workflow.

---

## 🎯 Purpose

This template is designed to:

- Provide a consistent structure for all new tools  
- Embed standardised metadata for indexing and version tracking  
- Support dry‑run, verbose, logging, and hash‑based audit modes  
- Encourage modular, readable, maintainable tool design  
- Enable AI‑assisted tool generation with minimal post‑editing  

Every tool created from this template will automatically conform to Toolbox standards.

---

## 🧪 Usage

To create a new tool:

1. Copy the template:
   ```bash
   cp template <toolname>
   ```

2. Update the metadata block:
   ```bash
   # Type / Version : bash / YYYY.MM.DD-00
   # Script Purpose : <describe the tool>
   ```

3. Replace `<toolname>` in:
   - `TOOL_NAME="<toolname>"`
   - Output file paths  
   - Usage examples  
   - Help block  

4. Implement your logic inside the `main()` function.

5. Use the helper functions:
   - `log "message"` for verbose output  
   - `run_step "command"` for dry‑run‑aware execution  

6. Validate the tool with:
   ```bash
   tool-box
   tool-box <toolname>
   ```

---

## 🧩 Embedded Features

| Feature         | Description                                                  |
|----------------|--------------------------------------------------------------|
| Metadata Block | Standardised `Type / Version`, `Script Purpose`, `Package`   |
| Flag Parsing   | Built‑in support for `--dry-run`, `--verbose`, `--log`, `--hashmap` |
| Logging        | Writes to `/var/log/<toolname>.log`                          |
| Hashmap        | Generates `.hashmap/<toolname>.hash` + timestamp             |
| Modular Logic  | Clean `main()` function with helper utilities                |
| Help Block     | Auto‑parsed by `tool-box` for indexing and documentation     |

---

## 🧠 Template Structure

The template includes:

- **Metadata block** for indexing  
- **Flag parser** for consistent behaviour  
- **Helper functions** (`log`, `run_step`)  
- **Main logic block** to be replaced per tool  
- **Logging and hashmap generation**  
- **Standardised output file locations**  

This ensures every tool behaves predictably and integrates cleanly.

---

## 🤖 AI Integration

This template is optimised for AI‑assisted development.

To generate a new tool, paste the template into your AI companion and request:

> “Generate a new Toolbox tool named `<toolname>` that performs `<function>`.”

The AI will return a fully structured script that already conforms to Toolbox standards.

---

## 🧭 Contributor Guidance

- Always start from `template`  
- Update the version using the Toolbox model:  
  ```
  YYYY.MM.DD-BUILD
  ```
- Keep logic modular and avoid hardcoded paths  
- Use `run_step` for any command that should respect dry‑run mode  
- Ensure output file paths match the tool name  
- Validate metadata and help formatting using:
  ```bash
  tool-box
  tool-box <toolname>
  ```

---

## 🤖 AI & Ethics Disclosure  

This template was co‑authored with AI assistance.  
For details on ethical integration, traceability, and responsible authorship, see:  
ethics_AI.md (github.com in Bing) (bing.com in Bing)

🔙 Return to [Toolbox](https://github.com/Mark-a-Hamilton/Toolbox)")
