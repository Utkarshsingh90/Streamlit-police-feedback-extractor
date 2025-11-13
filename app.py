import streamlit as st
import fitz  # PyMuPDF
from transformers import pipeline
import spacy
import json

# ---------- INITIAL SETUP ----------
st.set_page_config(page_title="Police Feedback Analyzer", layout="wide")
st.title("🚓 Smart Analytics: Police Feedback Analyzer")

@st.cache_resource
def load_models():
    sentiment_model = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
    topic_model = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
    nlp = spacy.load("en_core_web_md")
    return sentiment_model, topic_model, nlp

sentiment_model, topic_model, nlp = load_models()

# ---------- UTILITY FUNCTIONS ----------
def extract_text_from_pdf(uploaded_file):
    text = ""
    try:
        with fitz.open(stream=uploaded_file.read(), filetype="pdf") as doc:
            for page in doc:
                text += page.get_text()
    except Exception as e:
        st.error(f"PDF extraction error: {e}")
    return text.strip()

def extract_entities(text):
    doc = nlp(text)
    officers = []
    departments = []
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            officers.append(ent.text)
        elif "Police" in ent.text or "Station" in ent.text:
            departments.append(ent.text)
    return list(set(officers)), list(set(departments))

def analyze_feedback(text):
    sentiment_result = sentiment_model(text[:512])[0]  # analyze only first 512 chars
    sentiment_score = sentiment_result["score"] if sentiment_result["label"] == "POSITIVE" else -sentiment_result["score"]
    topics = topic_model(
        text,
        candidate_labels=["bravery", "community service", "investigation", "rescue", "discipline", "training", "traffic management"],
    )
    top_topics = [t for t, s in zip(topics["labels"], topics["scores"]) if s > 0.3]
    officers, departments = extract_entities(text)
    return {
        "officers": officers,
        "departments": departments,
        "sentiment_score": round(sentiment_score, 3),
        "sentiment_label": sentiment_result["label"],
        "topics": top_topics,
    }

# ---------- STREAMLIT UI ----------
uploaded_file = st.file_uploader("📤 Upload a feedback file (PDF or text)", type=["pdf", "txt"])

if uploaded_file:
    if uploaded_file.type == "application/pdf":
        text = extract_text_from_pdf(uploaded_file)
    else:
        text = uploaded_file.read().decode("utf-8")

    if text:
        st.subheader("📝 Extracted Text Preview")
        st.text_area("Text Content", text[:1000] + "...", height=200)

        with st.spinner("Analyzing feedback..."):
            results = analyze_feedback(text)

        st.success("✅ Analysis Complete")
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### 👮‍♂️ Detected Officers")
            st.write(results["officers"] or "No names detected")

            st.markdown("### 🏢 Departments")
            st.write(results["departments"] or "No departments detected")

        with col2:
            st.markdown("### 💬 Sentiment Analysis")
            st.metric("Sentiment", results["sentiment_label"], results["sentiment_score"])

            st.markdown("### 🏷️ Topic Tags")
            st.write(", ".join(results["topics"]) if results["topics"] else "No clear topic found")

        # Optional: Download JSON
        st.download_button(
            "⬇️ Download Results JSON",
            data=json.dumps(results, indent=2),
            file_name="feedback_analysis.json",
            mime="application/json",
        )
    else:
        st.warning("No text extracted. Try another file.")
else:
    st.info("Upload a feedback file to begin analysis.")
