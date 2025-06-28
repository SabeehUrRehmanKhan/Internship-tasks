# text_summarizer_app.py

import streamlit as st
from transformers import pipeline
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Load models
@st.cache_resource
def load_models():
    nlp = spacy.load("en_core_web_sm")
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    return nlp, summarizer

nlp, summarizer = load_models()

# Extractive summarization function
def extractive_summary(text, num_sentences=3):
    doc = nlp(text)
    sentences = [sent.text.strip() for sent in doc.sents if len(sent.text.strip()) > 10]
    if len(sentences) < num_sentences:
        return " ".join(sentences)
    tfidf = TfidfVectorizer().fit_transform(sentences)
    sim_matrix = cosine_similarity(tfidf)
    scores = sim_matrix.sum(axis=1)
    top_sentences = [sentences[i] for i in np.argsort(scores)[-num_sentences:]]
    return " ".join(top_sentences)

# Abstractive summarization function
def abstractive_summary(text):
    return summarizer(text, max_length=130, min_length=30, do_sample=False)[0]['summary_text']

# Streamlit UI
st.title("📝 Text Summarizer")

text_input = st.text_area("Paste an article, blog, or news content:", height=300)

summary_type = st.radio("Choose summarization method:", ["Extractive", "Abstractive"])

if st.button("Summarize"):
    if len(text_input.strip()) < 50:
        st.warning("Please provide a longer input for summarization.")
    else:
        with st.spinner("Summarizing..."):
            if summary_type == "Extractive":
                summary = extractive_summary(text_input)
            else:
                summary = abstractive_summary(text_input)
        st.subheader("Summary:")
        st.write(summary)
        st.success("Summary generated successfully!")