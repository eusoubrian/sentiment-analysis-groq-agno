import streamlit as st
import pandas as pd
from groq import Groq
import json
import time
from dotenv import load_dotenv
import altair as alt

load_dotenv()

client = Groq()

def analyze_sentiment(text):
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": """You are a data analysis API that performs sentiment analysis on text.
                    Respond only with JSON using this format:
                    {
                        "sentiment_analysis": {
                        "sentiment": "positive|negative|neutral",
                        "confidence_score": 0.95,
                        "key_phrases": [
                            {
                            "phrase": "detected key phrase",
                            "sentiment": "positive|negative|neutral"
                            }
                        ],
                        "summary": "One sentence summary of the overall sentiment"
                        }
                    }"""
                },
                {
                    "role": "user",
                    "content": f"Analyze the sentiment of this customer review: '{text}'"
                }
            ],
            response_format={"type": "json_object"}
        )

        result = json.loads(response.choices[0].message.content)
        return result["sentiment_analysis"]["sentiment"]
    except Exception as e:
        st.warning(f"Error analyzing review: {e}")
        return "error"

st.title("Sentiment Analysis with Groq + Streamlit")

uploaded_file = st.file_uploader("Upload a CSV file with a 'review_text' column", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    if "review_text" not in df.columns:
        st.error("The uploaded CSV must contain a column named 'review_text'")
    else:
        st.write(f"✅ Loaded {len(df)} reviews.")

        if st.button("Run Sentiment Analysis"):
            sentiments = []
            progress = st.progress(0)
            status = st.empty()

            for i, review in enumerate(df["review_text"]):
                status.text(f"Analyzing review {i+1}/{len(df)}...")
                sentiment = analyze_sentiment(str(review))
                sentiments.append(sentiment)
                progress.progress((i + 1) / len(df))
                time.sleep(0.25)

            df["sentiment"] = sentiments

            st.subheader("Sentiment Analysis Results")
            st.dataframe(df[["review_text", "sentiment"]])

            sentiment_counts = df["sentiment"].value_counts().reset_index()
            sentiment_counts.columns = ["sentiment", "count"]

            chart = alt.Chart(sentiment_counts).mark_bar().encode(
                x="sentiment:N",
                y="count:Q",
                color="sentiment:N"
            ).properties(
                title="Sentiment Distribution"
            )

            st.altair_chart(chart, use_container_width=True)

            csv = df.to_csv(index=False).encode("utf-8")
            st.download_button(
                label="Download results as CSV",
                data=csv,
                file_name="sentiment_results.csv",
                mime="text/csv"
            )
