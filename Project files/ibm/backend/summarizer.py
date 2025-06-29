import os
import httpx
from dotenv import load_dotenv

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")

async def summarize_text(text: str) -> str:
    url = "https://api-inference.huggingface.com/models/facebook/bart-large-cnn"

    headers = {
        "Authorization": f"Bearer {HF_TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "inputs": text,
        "parameters": {
            "max_length": 200,
            "min_length": 50,
            "do_sample": False
        }
    }

    async with httpx.AsyncClient(timeout=60) as client:
        response = await client.post(url, headers=headers, json=payload)

    if response.status_code != 200:
        raise Exception(f"Summarization error: {response.text}")

    result = response.json()
    return result[0]['summary_text']
