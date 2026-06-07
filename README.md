# Automated Motivation Classification: Intrinsic vs. Extrinsic

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
![Transformers](https://img.shields.io/badge/HuggingFace-Transformers-F9AB00?style=for-the-badge&logo=huggingface)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)

## 📖 About the Project

This repository houses an end-to-end Natural Language Processing (NLP) pipeline designed to classify conversational statements into **Intrinsic** or **Extrinsic** motivation. 

Initially analyzing raw mentorship dialogue, the architecture leverages a hybrid methodology:
1. **Zero-Shot Pseudo-Labeling:** Utilizes `facebook/bart-large-mnli` to parse mentor-entrepreneur conversations and extract initial classifications.
2. **Confidence Filtering:** Isolates highly reliable predictions (confidence > 88%) to build a high-quality, auto-generated dataset.
3. **Data Augmentation:** Rebalances the inherently skewed dataset to prevent bias towards extrinsic motivation.
4. **Supervised Fine-Tuning:** Fine-tunes `distilbert-base-uncased` on the augmented dataset to produce a fast, robust, and deployment-ready classification model.

An interactive Streamlit interface is included for real-time inference and demonstration.

---

## ⚙️ Prerequisites

- Python 3.9+
- GPU recommended for inference and fine-tuning (CUDA/MPS support built-in)

---

## 🚀 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Harsh-7612/Automated-Motivation-Classification-IntrinsicVSExtrinsic.git](https://github.com/Harsh-7612/Automated-Motivation-Classification-IntrinsicVSExtrinsic.git)
   cd Automated-Motivation-Classification-IntrinsicVSExtrinsic

2. create virtual environment:
   python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies:
   pip install -r requirements.txt
