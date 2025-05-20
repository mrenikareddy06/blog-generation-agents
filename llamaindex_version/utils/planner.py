from utils.agents import get_llm

def plan_topic(topic: str) -> str:
    llm = get_llm()
    prompt = f"You are a blog planner. Given the topic: '{topic}', generate a clear blog outline with 3-5 bullet points."
    return llm.complete(prompt).text.strip()
