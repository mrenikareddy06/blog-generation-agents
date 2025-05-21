import streamlit as st
from main import run_blog_generation
from dotenv import load_dotenv
load_dotenv()

st.title("📝 LlamaIndex Blog Generator")
topic = st.text_input("Enter a blog topic", "The Future of Open Source AI")

if st.button("Generate Blog"):
    if topic:
        with st.spinner("Planning blog outline..."):
            outputs = run_blog_generation(topic)

        st.subheader("📋 Blog Outline")
        st.markdown(outputs["outline"])

        st.subheader("🔍 Researched Context")
        st.markdown(outputs["context"])

        st.subheader("✍️ Initial Draft")
        st.markdown(outputs["draft"])

        st.subheader("✅ Final Polished Blog")
        st.markdown(outputs["final"])
    else:
        st.warning("Please enter a topic.")
