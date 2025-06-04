# Intonate
*A lightweight command-line engine that converts Markdown into expressive SSML for natural-sounding text-to-speech output.*

---

## 🚀 What It Does

**Intonate** is a rules-based preprocessor that scans plain text or Markdown and applies SSML tags (like `<break>`, `<prosody>`, `<emphasis>`) using a configurable YAML ruleset. It outputs voice-friendly SSML ready for use with TTS systems like ElevenLabs or Amazon Polly.

---

## ⚙️ How to Use

### ✅ Prerequisites
- Python 3.9+
- Install `pyyaml`:
  ```bash
  pip install pyyaml
  ```


### ▶️ CLI Usage

```bash
python3 engine.py --input input/sample.md --config config/default.yaml --output output/output.ssml
```


## 📁 Project Structure

```
intonate/
├── engine.py                 # Main CLI engine
├── config/
│   └── default.yaml          # YAML tagging rules
├── input/
│   └── sample.md             # Example Markdown input
├── output/
│   └── output.ssml           # SSML output
└── README.md                 # Project documentation
```

## ✨ Example Output

#### Input (sample.md):

# Introduction

This is a test of the Intonate engine.

## Features

- Lightweight
- Configurable
- Fun to build

#### Output (output.ssml):

<break time="500ms"/>Introduction

This is a test of the Intonate engine.

<break time="500ms"/>Features

<break time="200ms"/>Lightweight
<break time="200ms"/>Configurable
<break time="200ms"/>Fun to build


## 📌 Roadmap (Coming Soon)

- Support for <speak> wrapper

- Inline voice and emotion tags

- Speech Markdown output format

- Config profiles (e.g., "narrator", "tutorial", "story")

**Brian Shand**  
[GitHub Profile](https://github.com/brian-shand)  
📧 brianshand.dev@gmail.com
