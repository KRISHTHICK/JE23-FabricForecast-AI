import streamlit as st
from PIL import Image
from wardrobe_utils import analyze_wardrobe
from agent_planner import fashion_agent
from rag_helper import process_doc, ask_doc_question

st.set_page_config(page_title="🌿 FabricForecast AI", layout="wide")
st.title("🌿 FabricForecast AI – Climate-Aware Sustainable Fashion Advisor")

st.sidebar.header("1️⃣ Upload Fabric or Outfit Image")
img_file = st.sidebar.file_uploader("Upload Wardrobe Image", type=["jpg", "jpeg", "png"])

st.sidebar.header("2️⃣ Upload Sustainability PDF (optional)")
pdf_file = st.sidebar.file_uploader("Upload PDF", type=["pdf"])

if img_file:
    img = Image.open(img_file)
    st.image(img, caption="Your Wardrobe", use_container_width=True)

    with st.spinner("Analyzing wardrobe..."):
        summary = analyze_wardrobe(img)
    st.success("Wardrobe Analysis Complete ✅")
    st.markdown(summary)

st.divider()
st.subheader("🧠 Ask the AI Fashion Agent")
q = st.text_input("Ask for eco-friendly or weather-based outfit ideas:")
if q:
    answer = fashion_agent(q)
    st.markdown(answer)

if pdf_file:
    with st.spinner("Processing PDF..."):
        vector_store = process_doc(pdf_file)
        st.success("PDF Ready for Questions")

    st.subheader("📄 Ask questions from the uploaded document")
    pdf_q = st.text_input("Ask about sustainability report or textile standard:")
    if pdf_q:
        response = ask_doc_question(vector_store, pdf_q)
        st.markdown(response)

