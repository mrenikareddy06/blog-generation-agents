import streamlit as st
from main import generate_blog

st.set_page_config(page_title="AutoGen Blog Generator", page_icon="📝")
st.title("🧠 AutoGen Blog Generator")

topic = st.text_input("📝 Enter blog topic:", "The Future of Open Source AI")

if st.button("Generate Blog"):
    with st.spinner("Agents are generating collaboratively..."):
        result = generate_blog(topic)
        st.markdown("### 🗣️ Agent Conversations")
        for msg in result.chat_history:
            st.markdown(f"**{msg['role'].capitalize()}**: {msg['content']}\n\n")

        st.markdown("---")
        st.markdown("### Final Blog Output")
        try:
            blog = result.summary
            st.markdown(blog)
        except:
            st.warning("⚠️ Blog summary not captured.")
        st.success("Done!")
