# 📊 sentiment-analysis-groq-agno

A simple and interactive Streamlit application that performs **sentiment analysis** on user reviews using the **Groq API** powered by **LLaMA 3.3-70B** via the Agno framework.

Upload a CSV file with customer reviews, run the analysis, and visualize the overall sentiment distribution (positive, negative, neutral) — all in one click!

---

## 🚀 Features

- 📁 Upload any CSV file with a `review_text` column.
- 🧠 Uses Groq's LLaMA 3 model to detect sentiment via natural language.
- 📊 Interactive sentiment distribution chart (Altair).
- 💾 Option to download the analyzed results as a CSV.
- 🌐 Clean and intuitive UI powered by Streamlit.

---

## 🛠️ Installation

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/sentiment-analysis-groq-agno.git
cd sentiment-analysis-groq-agno

    Create a virtual environment (optional but recommended):

python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

    Install dependencies:

pip install -r requirements.txt

    Set up your Groq API key:

Create a .env file in the project root and add:

GROQ_API_KEY=your_groq_api_key_here

▶️ Usage

Run the Streamlit app:

streamlit run app.py

Then:

    Upload a CSV file with a column named review_text.

    Click "Run Sentiment Analysis".

    View and download the results.

📂 Example Input CSV

review_text
"I love this game, it's amazing!"
"This is the worst experience I've had."
"Meh, it's okay, nothing special."

📈 Output Example
review_text	sentiment
I love this game, it's amazing!	positive
This is the worst experience I've had.	negative
Meh, it's okay, nothing special.	neutral

A chart showing the distribution of sentiments will also be displayed.
📦 Requirements

    Python 3.8+

    Streamlit

    Pandas

    Altair

    Groq Python SDK

    python-dotenv

Install them with:

pip install streamlit pandas altair groq python-dotenv
