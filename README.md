<div align="center">

# ✍️ Grammar & Spell Checker

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/NLP-Powered-blueviolet?style=for-the-badge&logo=openai&logoColor=white"/>
  <img src="https://img.shields.io/badge/LanguageTool-Grammar%20Check-green?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/SpellCheck-PySpellChecker-orange?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/License-Apache%202.0-red?style=for-the-badge"/>
</p>

<p align="center">
  A Python-based <strong>Grammar & Spell Checking tool</strong> powered by NLP.<br/>
  Detects spelling mistakes, grammar errors, and punctuation issues — and suggests corrections automatically.
</p>

<p align="center">
  <a href="#-overview">Overview</a> •
  <a href="#-features">Features</a> •
  <a href="#-how-it-works">How It Works</a> •
  <a href="#-installation">Installation</a> •
  <a href="#-usage">Usage</a> •
  <a href="#-example-output">Example</a> •
  <a href="#-contributing">Contributing</a>
</p>

</div>

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [How It Works](#-how-it-works)
- [Project Structure](#-project-structure)
- [Tech Stack](#-tech-stack)
- [Installation](#-installation)
- [Usage](#-usage)
- [Error Types Detected](#-error-types-detected)
- [Example Output](#-example-output)
- [Use Cases](#-use-cases)
- [Troubleshooting](#-troubleshooting)
- [Future Enhancements](#-future-enhancements)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🧠 Overview

**Grammar-and-spell-checker** is a Python NLP project that automatically detects and corrects:
- ❌ Spelling mistakes
- ❌ Grammar errors (subject-verb agreement, tense, articles)
- ❌ Punctuation issues
- ❌ Word usage errors

It follows a clean **two-layer architecture** — `Model.py` handles the NLP logic while `app.py` manages the user-facing interface. A sample `text.txt` is included for quick testing.

---

## ✨ Features

- 🔤 **Spell checking** — detects and corrects misspelled words
- 📐 **Grammar checking** — identifies grammatical rule violations
- 💡 **Smart suggestions** — provides one or more correction options per error
- 📄 **File input support** — reads from `text.txt` directly
- 🏗️ **Modular architecture** — Model and App layers separated cleanly
- ⚡ **Lightweight** — no heavy dependencies, quick setup

---

## ⚙️ How It Works

```
Input Text (typed / from text.txt)
              │
              ▼
┌─────────────────────────────────────────┐
│               app.py                    │
│  ┌───────────────────────────────────┐  │
│  │  1. Read Input                    │  │  ← Direct string or text.txt file
│  └──────────────┬────────────────────┘  │
│                 │                        │
│  ┌──────────────▼────────────────────┐  │
│  │  2. Pass to Model                 │  │  ← Calls Model.py functions
│  └──────────────┬────────────────────┘  │
└─────────────────┼────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────┐
│               Model.py                  │
│                                         │
│  ┌───────────────────────────────────┐  │
│  │  3. Spell Check                   │  │  ← PySpellChecker / TextBlob
│  │     - Tokenize words              │  │     detects unknown words
│  │     - Compare against dictionary  │  │     suggests corrections
│  └──────────────┬────────────────────┘  │
│                 │                        │
│  ┌──────────────▼────────────────────┐  │
│  │  4. Grammar Check                 │  │  ← LanguageTool / language_tool_python
│  │     - Rule-based NLP analysis     │  │     checks 1000+ grammar rules
│  │     - POS tagging                 │  │
│  └──────────────┬────────────────────┘  │
│                 │                        │
│  ┌──────────────▼────────────────────┐  │
│  │  5. Compile Errors & Suggestions  │  │  ← Returns list of issues
│  └──────────────┬────────────────────┘  │
└─────────────────┼────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────┐
│   Output: Errors + Corrected Text       │
└─────────────────────────────────────────┘
```

---

## 🗂️ Project Structure

```
Grammar-and-spell-checker/
│
├── 🐍 app.py         # Entry point — handles I/O, calls Model functions
├── 🐍 Model.py       # Core NLP logic — spell & grammar checking engine
├── 📝 text.txt       # Sample input text for testing
├── 📄 LICENSE        # Apache 2.0
└── 📄 README.md      # You are here
```

### Responsibility Breakdown

| File | Role |
|---|---|
| `app.py` | User interface layer — reads input, displays output, orchestrates flow |
| `Model.py` | Business logic layer — NLP processing, error detection, suggestions |
| `text.txt` | Sample text with intentional errors for demo/testing |

---

## 🛠️ Tech Stack

| Library | Purpose |
|---|---|
| `Python 3.8+` | Core language |
| `language-tool-python` | Grammar checking via LanguageTool (1000+ rules) |
| `pyspellchecker` | Dictionary-based spell checking |
| `textblob` *(optional)* | Alternative spell correction via TextBlob |
| `nltk` | Tokenization, POS tagging, stopword handling |

---

## 📦 Installation

**1. Clone the repository:**
```bash
git clone https://github.com/eddiebrock911/Grammar-and-spell-checker.git
cd Grammar-and-spell-checker
```

**2. Create & activate a virtual environment:**
```bash
# Create
python -m venv venv

# Activate — Linux/Mac
source venv/bin/activate

# Activate — Windows
venv\Scripts\activate
```

**3. Install dependencies:**
```bash
pip install language-tool-python pyspellchecker nltk textblob
```

**4. Download NLTK data (if required):**
```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
```

> ⚠️ `language-tool-python` downloads the LanguageTool JAR (~200MB) on first run. Java (JRE 8+) must be installed.

---

## ▶️ Usage

### Run the app:
```bash
python app.py
```

### Check text from `text.txt`:
Add your text to `text.txt`, then run `app.py` — it reads and processes the file automatically.

### Use Model directly in your code:

```python
from Model import check_spelling, check_grammar

text = "She go to school everyday and she dont likes it."

# Spell Check
spell_errors = check_spelling(text)
for word, suggestion in spell_errors.items():
    print(f"❌ Spelling: '{word}' → ✅ '{suggestion}'")

# Grammar Check
grammar_errors = check_grammar(text)
for error in grammar_errors:
    print(f"❌ Grammar: {error.message}")
    print(f"   Context: {error.context}")
    print(f"   ✅ Suggestion: {error.replacements[:3]}")
```

### Programmatic full pipeline:
```python
from Model import check_spelling, check_grammar, apply_corrections

text = "Thier going to the store but they doesnt have money."

corrected = apply_corrections(text)
print("Original :", text)
print("Corrected:", corrected)
```

---

## 🔍 Error Types Detected

| Category | Error Type | Example |
|---|---|---|
| **Spelling** | Misspelled word | `thier` → `their` |
| **Spelling** | Missing letter | `recieve` → `receive` |
| **Grammar** | Subject-verb agreement | `She go` → `She goes` |
| **Grammar** | Wrong tense | `He goed` → `He went` |
| **Grammar** | Missing article | `I have dog` → `I have a dog` |
| **Grammar** | Double negative | `I don't know nothing` → `I don't know anything` |
| **Punctuation** | Missing comma | `Hello John` → `Hello, John` |
| **Punctuation** | Extra space | `word  word` → `word word` |
| **Word Usage** | Wrong preposition | `depends of` → `depends on` |
| **Word Usage** | Confused words | `their/there/they're` |

---

## 📋 Example Output

**Input (`text.txt`):**
```
She go to school everyday and she dont likes it.
Their are many student in the clasroom who doesnt no the anser.
```

**Output:**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 SPELL CHECK RESULTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
❌ 'clasroom'   → ✅ 'classroom'
❌ 'doesnt'     → ✅ "doesn't"
❌ 'anser'      → ✅ 'answer'

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 GRAMMAR CHECK RESULTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
❌ [Line 1] Subject-verb agreement error
   "She go"  →  ✅ "She goes"

❌ [Line 1] Contraction error
   "dont likes"  →  ✅ "doesn't like"

❌ [Line 2] Wrong word usage
   "Their are"  →  ✅ "There are"

❌ [Line 2] Plural agreement
   "many student"  →  ✅ "many students"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 CORRECTED TEXT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
She goes to school every day and she doesn't like it.
There are many students in the classroom who don't know the answer.
```

---

## 💡 Use Cases

| Domain | Application |
|---|---|
| 📝 **Writing Tools** | Blog post / essay grammar correction |
| 🎓 **Education** | Student writing feedback system |
| 📧 **Email Clients** | Auto-correct before sending |
| 💬 **Chat Apps** | Real-time spell check in messaging |
| 🤖 **NLP Pipelines** | Text cleaning before ML model training |
| 🌐 **Content Management** | CMS editor grammar validation |

---

## 🐛 Troubleshooting

| Problem | Solution |
|---|---|
| `Java not found` error | Install Java JRE 8+: [java.com/download](https://java.com/download) |
| `language_tool_python` download fails | Check internet; ~200MB download on first run |
| `ModuleNotFoundError` | Run `pip install language-tool-python pyspellchecker` |
| Grammar check too slow | Use `language_tool_python.utils.close_port()` after use |
| NLTK `punkt` not found | Run `nltk.download('punkt')` in Python shell |
| Incorrect suggestions | Lower confidence threshold in `Model.py` logic |

---

## 🚀 Future Enhancements

- [ ] 🌐 Streamlit / Flask web UI for browser-based checking
- [ ] 🌍 Multi-language support (Spanish, French, German)
- [ ] 🤗 Transformer-based grammar correction (T5, BERT)
- [ ] 📊 Error statistics dashboard
- [ ] 🔌 VS Code extension integration
- [ ] 📱 REST API for third-party integrations
- [ ] 📂 Batch processing of multiple `.txt` files

---

## 🤝 Contributing

Contributions are always welcome!

```bash
# 1. Fork the repo on GitHub

# 2. Clone your fork
git clone https://github.com/your-username/Grammar-and-spell-checker.git

# 3. Create a feature branch
git checkout -b feature/your-feature-name

# 4. Make your changes & commit
git commit -m "feat: describe your change"

# 5. Push & open a Pull Request
git push origin feature/your-feature-name
```

Please follow [PEP 8](https://pep8.org/) coding style for all Python contributions.

---

## 📄 License

This project is licensed under the **Apache 2.0 License** — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

Made with ❤️ by [eddiebrock911](https://github.com/eddiebrock911)

⭐ **Star this repo** if it helped you write better!

</div>
