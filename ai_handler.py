import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))
MODEL = "llama-3.3-70b-versatile"


def is_api_configured() -> bool:
    return os.getenv("GROQ_API_KEY") is not None


def get_response(messages: list) -> str:
    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        max_tokens=1000,
    )
    return response.choices[0].message.content


def get_streaming_response(messages: list):
    stream = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        max_tokens=1000,
        stream=True,
    )
    for chunk in stream:
        delta = chunk.choices[0].delta.content
        if delta:
            yield delta