import streamlit as st
from main import run_crew

st.set_page_config(page_title="CrewAI Content Generator", page_icon="🧠")
st.title("🧠 CrewAI Content Generator")
st.markdown("Generate polished blog posts using multi-agent LLM workflows.")

with st.form("crewai_form"):
    topic = st.text_input("📝 Enter a topic:", "The Future of Open Source AI")
    submit = st.form_submit_button("Generate Blog")

if submit:
    with st.spinner("Running agents... hang tight"):
        output = run_crew(topic)
        st.markdown("### Final Blog Output")
        st.markdown(output)
        st.success("All done!")