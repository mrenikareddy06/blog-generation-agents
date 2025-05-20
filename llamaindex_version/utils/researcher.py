from utils.agents import get_llm

def fetch_context(outline: str) -> str:
    llm = get_llm()
    prompt = f"Given the outline:\n{outline}\nResearch and expand it with relevant factual information."
    return llm.complete(prompt).text.strip()
