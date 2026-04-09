import streamlit as st
from newspaper import Article
from textblob import TextBlob
import nltk

nltk.download('punkt')
nltk.download('punkt_tab')

st.title("📰 News Summarizer + Sentiment Analyzer")

url = st.text_input("Enter News Article URL")

if st.button("Summarize"):

    if url == "":
        st.warning("Please enter a URL")
    else:
        article = Article(url)

        article.download()
        article.parse()
        article.nlp()

        st.subheader("Title")
        st.write(article.title)

        st.subheader("Authors")
        st.write(article.authors)

        st.subheader("Publish Date")
        st.write(article.publish_date)

        st.subheader("Summary")
        st.write(article.summary)

        analysis = TextBlob(article.text)
        polarity = analysis.sentiment.polarity

        st.subheader("Sentiment")

        if polarity > 0:
            st.success("😊 Positive")
        elif polarity < 0:
            st.error("😡 Negative")
        else:
            st.info("😐 Neutral")
