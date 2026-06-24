from groq import Groq
from app.config import config


class LLMClient:
    """Thin wrapper around the Groq API.

    The rest of the app talks only to this class, never to Groq directly,
    so the provider can be swapped by changing only this file.
    """

    def __init__(self):
        config.validate()
        self.client = Groq(api_key=config.GROQ_API_KEY)
        self.model = config.LLM_MODEL

    def generate(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
        )
        return response.choices[0].message.content


llm = LLMClient()
