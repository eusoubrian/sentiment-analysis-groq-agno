# 📊 sentiment-analysis-groq

An interactive Streamlit application that performs **sentiment analysis** on customer reviews using the **Groq API**, powered by **LLaMA 3.3-70B**

Upload a CSV file containing reviews, run the analysis, and visualize the sentiment distribution — all in a clean and intuitive interface.

---

## 🚀 Features

- 📁 Upload CSV files with a `review_text` column
- 🤖 Sentiment analysis using Groq's LLaMA 3 model
- 📊 Interactive sentiment distribution chart (via Altair)
- 💾 Download analyzed results as CSV
- 🌐 User-friendly interface with Streamlit

---

## 🛠️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/sentiment-analysis-groq-agno.git
cd sentiment-analysis-groq-agno
```

### 2. Create a virtual environment (optional but recommended)

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set your Groq API key
Create a .env file in the root directory and add your Groq API key:

```bash
GROQ_API_KEY=your_groq_api_key_here
```

### ▶️ Usage

To launch the app:

```bash
streamlit run app.py
```

### 📂 Example Input CSV

```bash
review_text
"I love this game, it's amazing!"
"This is the worst experience I've had."
"Meh, it's okay, nothing special."
```

