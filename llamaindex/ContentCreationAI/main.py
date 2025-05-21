from utils.planner import plan_topic
from utils.researcher import fetch_context
from utils.writer import generate_blog
from utils.editor import polish_blog
from dotenv import load_dotenv
load_dotenv()

def run_blog_generation(topic: str) -> dict:
    outline = plan_topic(topic)
    context = fetch_context(outline)
    blog = generate_blog(context)
    polished = polish_blog(blog)
    
    return {
        "outline": outline,
        "context": context,
        "draft": blog,
        "final": polished
    }
