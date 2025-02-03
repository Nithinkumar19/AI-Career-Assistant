from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
import os

def load_llm(llm_name):  
    llm = None  # Initialize llm to avoid errors

    if llm_name == 'openai':
        openai_key = os.getenv("OPENAI_API_KEY")
        if not openai_key:
            raise ValueError("OPENAI_API_KEY is not set in environment variables.")
        llm = ChatOpenAI(model_name="gpt-4o-mini", openai_api_key=openai_key, temperature=0.1, streaming=True)  

    elif llm_name == 'groq':
        groq_key = os.getenv("GROQ_API_KEY")
        if not groq_key:
            raise ValueError("GROQ_API_KEY is not set in environment variables.")
        llm = ChatGroq(temperature=0.2, groq_api_key=groq_key, model_name="llama3-70b-8192")

    elif llm_name == "llama3":
        llm = ChatOpenAI(model="llama3", base_url="http://localhost:11434/v1", temperature=0.0)

    else:
        raise ValueError(f"Invalid LLM name: {llm_name}. Choose from ['openai', 'groq', 'llama3'].")

    return llm
