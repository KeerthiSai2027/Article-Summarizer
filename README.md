# 📰 Article Summarizer

A modern AI-powered web application that extracts, summarizes, and analyzes news articles from any URL in seconds.

---

## 🚀 Live Demo

👉 https://article-summarizer2026.streamlit.app/
---

## ✨ Features

* 🔗 Input any news article URL
* 🧠 Automatic article summarization
* ✍️ Extracts authors and publish date
* 📊 Sentiment analysis (Positive / Negative / Neutral)
* 🧠 Keyword extraction
* 📄 Optional full article view
* 🧊 Modern glassmorphism UI
* 📥 Download summary as a text file

---

## 🛠️ Tech Stack

* **Python**
* **Streamlit**
* **Newspaper3k**
* **TextBlob**
* **NLTK**

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/Article-Summarizer.git
cd Article-Summarizer
```

Create virtual environment (recommended):

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Download required NLP data:

```bash
python -m textblob.download_corpora
```

---

## ▶️ Run Locally

```bash
streamlit run app.py
```

Open in browser:

```
http://localhost:8501
```

---

## 🌐 Deployment

This application is deployed using **Streamlit Cloud**.

Steps:

1. Push your code to GitHub
2. Connect repository to Streamlit Cloud
3. Deploy `app.py`

---
