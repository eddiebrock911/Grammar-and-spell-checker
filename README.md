# 📝 Grammar and Spell Checker

A Python-based grammar and spell checking tool that leverages NLP techniques to detect and correct grammatical errors and spelling mistakes in text.

## 🚀 Features

- ✅ Spell checking and correction
- ✅ Grammar error detection
- ✅ Supports plain text input (via `text.txt` or direct input)
- ✅ Clean and modular Python codebase

## 🗂️ Project Structure

```
Grammar-and-spell-checker/
│
├── app.py          # Main application entry point
├── Model.py        # Core grammar/spell checking model logic
├── text.txt        # Sample input text file
├── LICENSE         # Apache 2.0 License
└── README.md       # Project documentation
```

## 🛠️ Installation

**1. Clone the repository:**
```bash
git clone https://github.com/eddiebrock911/Grammar-and-spell-checker.git
cd Grammar-and-spell-checker
```

**2. Install dependencies:**
```bash
pip install -r requirements.txt
```

> If `requirements.txt` is not present, install common dependencies manually:
```bash
pip install language-tool-python pyspellchecker
```

## ▶️ Usage

**Run the app:**
```bash
python app.py
```

**To check text from file:**
- Add your text to `text.txt`
- Run `app.py` — it will read and process the file automatically

## 🧠 How It Works

1. **`Model.py`** — Contains the core logic for loading the NLP model, processing input text, detecting grammar/spelling errors, and returning suggestions.
2. **`app.py`** — Acts as the interface layer; takes user input (or reads from `text.txt`), calls the Model, and displays results.

## 📋 Example

**Input:**
```
She go to school everyday and she dont like it.
```

**Output:**
```
❌ Error: "go" → ✅ Suggestion: "goes"
❌ Error: "dont" → ✅ Suggestion: "doesn't"
```

## 📄 License

This project is licensed under the [Apache 2.0 License](LICENSE).

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

1. Fork the repo
2. Create your feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a Pull Request

## 👤 Author

**eddiebrock911**  
GitHub: [@eddiebrock911](https://github.com/eddiebrock911)
