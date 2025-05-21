import os
import autogen
from dotenv import load_dotenv
from utils.load_dotenv import load_environment

load_environment()
api_key = os.getenv("OPENAI_API_KEY")

llm_config = {
    "model": "llama3:8b",
    "base_url": "http://localhost:11434/v1",  
    "api_key": api_key,
}

planner = autogen.AssistantAgent(
    name="Planner",
    system_message="You're a content planner. Create a well-structured blog outline and content plan on the topic. Include SEO focus.",
    llm_config=llm_config,
)

writer = autogen.AssistantAgent(
    name="Writer",
    system_message="You're a professional blog writer. Write a compelling article in markdown using the Planner’s outline. Use 3–4 sections and a CTA.",
    llm_config=llm_config,
)

editor = autogen.AssistantAgent(
    name="Editor",
    system_message="You're an editor. Improve the Writer’s blog for grammar, flow, tone, and brand consistency.",
    llm_config=llm_config,
)

critic = autogen.AssistantAgent(
    name="Critic",
    system_message="You're a critic. Review the blog and provide feedback. Then send it to reviewers for SEO, legal, ethical, and final approval.",
    llm_config=llm_config,
)

seo = autogen.AssistantAgent(
    name="SEO_Reviewer",
    system_message="You're an SEO expert. Give 2–3 bullet-point suggestions to improve search engine visibility.",
    llm_config=llm_config,
)

legal = autogen.AssistantAgent(
    name="Legal_Reviewer",
    system_message="You're a legal reviewer. Ensure the content follows basic compliance and is risk-free.",
    llm_config=llm_config,
)

ethics = autogen.AssistantAgent(
    name="Ethics_Reviewer",
    system_message="You're an ethics reviewer. Flag any ethical concerns, such as bias or exclusion.",
    llm_config=llm_config,
)

meta = autogen.AssistantAgent(
    name="Meta_Reviewer",
    system_message="You're the meta reviewer. Aggregate the feedback and give a final judgment.",
    llm_config=llm_config,
)

review_chats = [
    {
        "recipient": seo,
        "message": lambda r, m, s, c: f"SEO review of the blog:\n\n{writer.chat_messages_for_summary(editor)[-1]['content']}",
        "max_turns": 1
    },
    {
        "recipient": legal,
        "message": lambda r, m, s, c: f"Legal review of the blog:\n\n{writer.chat_messages_for_summary(editor)[-1]['content']}",
        "max_turns": 1
    },
    {
        "recipient": ethics,
        "message": lambda r, m, s, c: f"Ethics review of the blog:\n\n{writer.chat_messages_for_summary(editor)[-1]['content']}",
        "max_turns": 1
    },
    {
        "recipient": meta,
        "message": "Please summarize all reviewer feedback and give your final suggestion.",
        "max_turns": 1
    }
]

critic.register_nested_chats(review_chats, trigger=writer)

def generate_blog(topic="The Future of Open Source AI", max_turns=4):
    task = f"Create a blog post about: {topic}"

    chat_result = critic.initiate_chat(
        recipient=editor,
        message=task,
        max_turns=max_turns,
        summary_method="reflection_with_llm",
    )

    return chat_result
