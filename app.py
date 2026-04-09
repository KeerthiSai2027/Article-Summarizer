import streamlit as st
from newspaper import Article
from textblob import TextBlob
import nltk

# NLTK setup
nltk.download('punkt')
nltk.download('punkt_tab')

# Page config
st.set_page_config(page_title="NewsAI Ultra", page_icon="🚀", layout="wide")

# CSS (Ultra UI)
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #0f172a, #020617);
}
.main {
    color: white;
}
.glass {
    background: rgba(255,255,255,0.05);
    border-radius: 20px;
    padding: 25px;
    backdrop-filter: blur(15px);
    box-shadow: 0 8px 32px rgba(0,0,0,0.4);
    margin-bottom: 20px;
}
.big-title {
    text-align: center;
    font-size: 52px;
    font-weight: 800;
}
.sub {
    text-align: center;
    color: #94a3b8;
    margin-bottom: 30px;
}
</style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("⚙️ Settings")
show_full_text = st.sidebar.checkbox("Show Full Article")
show_keywords = st.sidebar.checkbox("Show Keywords")

# Header
st.markdown('<div class="big-title">🚀 NewsAI Ultra</div>', unsafe_allow_html=True)
st.markdown('<div class="sub">AI-powered News Intelligence Dashboard</div>', unsafe_allow_html=True)

# Input
url = st.text_input("🔗 Paste Article URL")

if st.button("⚡ Analyze"):

    if not url:
        st.warning("Enter a valid URL")
    else:
        with st.spinner("Processing..."):

            article = Article(url)
            article.download()
            article.parse()
            article.nlp()

            analysis = TextBlob(article.text)
            polarity = analysis.sentiment.polarity

        # Layout
        col1, col2, col3 = st.columns([2,1,1])

        # Title + Summary
        with col1:
            st.markdown(f'<div class="glass"><h2>🧠 {article.title}</h2></div>', unsafe_allow_html=True)
            st.markdown(f'<div class="glass"><h3>📄 Summary</h3>{article.summary}</div>', unsafe_allow_html=True)

        # Meta Info
        with col2:
            st.markdown(f'<div class="glass"><b>✍️ Authors:</b><br>{article.authors}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="glass"><b>📅 Date:</b><br>{article.publish_date}</div>', unsafe_allow_html=True)

        # Sentiment
        with col3:
            st.markdown('<div class="glass"><h3>📊 Sentiment</h3></div>', unsafe_allow_html=True)

            score = (polarity + 1) / 2  # normalize 0–1
            st.progress(score)

            if polarity > 0:
                st.success(f"😊 Positive ({polarity:.2f})")
            elif polarity < 0:
                st.error(f"😡 Negative ({polarity:.2f})")
            else:
                st.info("😐 Neutral")

        # Keywords
        if show_keywords:
            st.markdown('<div class="glass"><h3>🧠 Keywords</h3></div>', unsafe_allow_html=True)
            st.write(article.keywords)

        # Full Text
        if show_full_text:
            with st.expander("📜 Full Article"):
                st.write(article.text)

        # Actions
        st.markdown('<div class="glass"><h3>⚡ Actions</h3></div>', unsafe_allow_html=True)

        colA, colB = st.columns(2)

        with colA:
            st.download_button(
                "📥 Download Summary",
                article.summary,
                file_name="summary.txt"
            )

        with colB:
            st.code(article.summary, language="text")