from utils.agents import get_llm

def generate_blog(researched_content: str) -> str:
    llm = get_llm()
    prompt = f"Using the following content:\n{researched_content}\nWrite a full blog article with intro, body, and conclusion."
    return llm.complete(prompt).text.strip()
