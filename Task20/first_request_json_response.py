
import os
import json

from dotenv import load_dotenv
from openai import OpenAI


# --------------------------------------------------
# 1. Load environment variables
# --------------------------------------------------

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
model = os.getenv("GROQ_MODEL")

if not api_key:
    raise RuntimeError("GROQ_API_KEY is missing.")

if not model:
    raise RuntimeError("GROQ_MODEL is missing.")


# --------------------------------------------------
# 2. Initialize Groq API client
# --------------------------------------------------

client = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1",
    timeout=30.0,
    max_retries=2,
)


# --------------------------------------------------
# 3. Define system instructions
# --------------------------------------------------

system_prompt = """
You are an ecommerce customer support assistant.

Your responsibilities:
- Answer customer questions about products.
- Explain product features.
- Help customers understand product availability.

Rules:
- Only use the product information provided.
- Never invent product prices or stock availability.
- Never assume product features that are not specified.
- If information is missing, clearly say so.
- Be friendly and concise.
- Limit your answer to three sentences.
"""


# --------------------------------------------------
# 4. Define product information
# --------------------------------------------------

product = {
    "name": "Wireless Gaming Mouse",
    "price": 35.00,
    "currency": "USD",
    "stock": 12,
    "connection": "Bluetooth and USB receiver",
    "color": "Black"
}

product_response_schema = {
    "type": "object",
    "properties": {
        "answer": {
            "type": "string"
        },
        "available": {
            "type": "boolean"
        },
        "price": {
            "type": "number"
        },
        "currency": {
            "type": "string"
        }
    },
    "required": [
        "answer",
        "available",
        "price",
        "currency"
    ],
    "additionalProperties": False
}

response_format={
    "type": "json_schema",
    "json_schema": {
        "name": "product_response",
        "strict": True,
        "schema": product_response_schema
    }
}

# --------------------------------------------------
# 5. Define user prompt
# --------------------------------------------------

user_prompt = f"""
Here is the product information:

{json.dumps(product, indent=2)}

Customer question:
Does this mouse support Bluetooth, and is it available?
"""


# --------------------------------------------------
# 6. Send request to Groq
# --------------------------------------------------

try:

    response = client.chat.completions.create(
        model=model,

        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ],

        response_format=response_format,

        max_completion_tokens=200,
    )


    # --------------------------------------------------
    # 7. Extract assistant response
    # --------------------------------------------------

    result = json.loads(
        response.choices[0].message.content
    )

    print(f"Answer: {result['answer']}")
    print(f"Available: {result['available']}")
    print(f"Price: {result['price']}")
    print(f"Currency: {result['currency']}")

    # --------------------------------------------------
    # 8. Display token usage
    # --------------------------------------------------

    if response.usage:
        print("\nToken Usage:")
        print(f"Input tokens: {response.usage.prompt_tokens}")
        print(f"Output tokens: {response.usage.completion_tokens}")
        print(f"Total tokens: {response.usage.total_tokens}")


except Exception as exc:

    print(f"Request failed: {type(exc).__name__}: {exc}")
