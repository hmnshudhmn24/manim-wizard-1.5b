
# Manim Wizard 1.5B

A domain-specialized **Qwen-Coder fine-tune** focused on the **Manim animation library**, designed to generate clean, correct, and structured mathematical animations from natural language prompts.

---

## ✨ Overview

**Manim Wizard 1.5B** is built for developers, educators, and researchers who want to create **Manim animations using plain English instructions**.

The model understands:
- Manim scene structure
- Mathematical visualization patterns
- Clean, readable Python animation code

---

## 🚀 Features

- Generates valid **Manim (Python)** code
- Focused on mathematical animations
- Clean `Scene` and class structure
- Fine-tuned using **LoRA**
- Lightweight and efficient
- Hugging Face compatible
- Code-only, reproducible setup

---

## 🧠 Base Model

- **Qwen-Coder 1.5B**

---

## 📁 Project Structure

```
manim-wizard-1.5b/
├── data/
│   └── manim_instructions.jsonl
├── training/
│   └── finetune_lora.py
├── inference/
│   └── generate_manim.py
├── eval/
│   └── eval_codegen.py
├── scripts/
│   └── prepare_repo.py
├── requirements.txt
├── .gitattributes
├── LICENSE
└── README.md
```

---

## 🛠️ Requirements

- Python 3.9+
- CUDA-enabled GPU (recommended)
- Manim installed locally
- Access to Qwen-Coder base model

```bash
pip install -r requirements.txt
```

---

## 📚 Dataset

Training samples are stored in:

```
data/manim_instructions.jsonl
```

Format:
```json
{
  "instruction": "Create a Manim animation of a sine wave",
  "response": "from manim import *\nimport numpy as np\n\nclass SineWave(Scene):\n    def construct(self):\n        ..."
}
```

---

## 🏋️ Training (LoRA Fine-Tuning)

```bash
python training/finetune_lora.py
```

---

## 🧪 Inference

```bash
python inference/generate_manim.py
```

---

## 🧪 Evaluation

```bash
python eval/eval_codegen.py
```

---

## ⚠️ Important Notes

- This repository contains **code only**
- Model weights are **not included**
- Upload trained weights to **Hugging Face**, not GitHub
- Use **Git LFS** if storing large files locally

---

## 🎯 Use Cases

- Math education videos
- Visual explanations
- YouTube & course content
- Rapid Manim prototyping
- Code-generation research

---

## 📜 License

Apache License 2.0

---

**Turn math ideas into animations — instantly.**
