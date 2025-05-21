from utils.agents import get_llm

def polish_blog(blog: str) -> str:
    llm = get_llm()
    prompt = f"Improve this blog for grammar, clarity, and flow:\n\n{blog}"
    return llm.complete(prompt).text.strip()
