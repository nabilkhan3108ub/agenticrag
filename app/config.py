import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """Central place for all settings. Read once, used everywhere."""

    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    LLM_MODEL = "llama-3.3-70b-versatile"  # free, capable model on Groq

    @classmethod
    def validate(cls):
        if not cls.GROQ_API_KEY:
            raise ValueError("GROQ_API_KEY not found. Check your .env file.")


config = Config()
