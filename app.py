import streamlit as st
from newspaper import Article
from textblob import TextBlob
import nltk

# Download NLTK data
nltk.download('punkt')
nltk.download('punkt_tab')

# Page config
st.set_page_config(page_title="News AI", page_icon="📰", layout="centered")

# Custom CSS
st.markdown("""
<style>
body {
    background-color: #0e1117;
}
.main {
    background-color: #0e1117;
    color: white;
}
.card {
    padding: 20px;
    border-radius: 15px;
    background-color: #161b22;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.3);
    margin-bottom: 20px;
}
.title {
    text-align: center;
    font-size: 40px;
    font-weight: bold;
}
.subtitle {
    text-align: center;
    color: #9ca3af;
    margin-bottom: 30px;
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="title">📰 News AI</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Summarize any article in seconds</div>', unsafe_allow_html=True)

# Input
url = st.text_input("🔗 Paste your news article URL")

# Button
if st.button("✨ Summarize"):

    if url == "":
        st.warning("Please enter a URL")
    else:
        with st.spinner("Analyzing article... ⏳"):

            article = Article(url)
            article.download()
            article.parse()
            article.nlp()

            # Sentiment
            analysis = TextBlob(article.text)
            polarity = analysis.sentiment.polarity

        # Title
        st.markdown(f'<div class="card"><h3>🧠 Title</h3>{article.title}</div>', unsafe_allow_html=True)

        # Authors
        st.markdown(f'<div class="card"><h3>✍️ Authors</h3>{article.authors}</div>', unsafe_allow_html=True)

        # Date
        st.markdown(f'<div class="card"><h3>📅 Publish Date</h3>{article.publish_date}</div>', unsafe_allow_html=True)

        # Summary
        st.markdown(f'<div class="card"><h3>📄 Summary</h3>{article.summary}</div>', unsafe_allow_html=True)

        # Sentiment
        if polarity > 0:
            sentiment = "😊 Positive"
        elif polarity < 0:
            sentiment = "😡 Negative"
        else:
            sentiment = "😐 Neutral"

        st.markdown(f'<div class="card"><h3>📊 Sentiment</h3>{sentiment}</div>', unsafe_allow_html=True)