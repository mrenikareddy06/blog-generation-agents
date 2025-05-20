from llama_index.llms.ollama import Ollama
import os

def get_llm():
    return Ollama(
        model=os.getenv("LLM_MODEL", "llama3:8b"),
        base_url=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434"),
        temperature=0.7,
        request_timeout=1800,  
        additional_kwargs={
            "stream": False  
        },
    )
