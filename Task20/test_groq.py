
import os

from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
model = os.getenv("GROQ_MODEL")

if not api_key:
    raise RuntimeError("GROQ_API_KEY is missing.")

if not model:
    raise RuntimeError("GROQ_MODEL is missing.")

# Connect to Groq using the OpenAI-compatible SDK
client = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1",
    timeout=30.0,
    max_retries=2,
)

try:
    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a helpful AI tutor. "
                    "Explain technical concepts in simple language."
                )
            },
            {
                "role": "user",
                "content": (
                    "Explain machine learning in simple terms."
                )
            }
        ],
        max_tokens=200,
    )

    answer = response.choices[0].message.content

    print("LLM response:")
    print(answer)

    print("\nToken usage:")
    print(response.usage)

except Exception as exc:
    print(f"Request failed: {type(exc).__name__}: {exc}")
