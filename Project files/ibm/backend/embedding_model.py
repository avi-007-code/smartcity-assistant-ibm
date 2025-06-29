import os
import httpx
from dotenv import load_dotenv

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")

async def get_embedding(text: str):
    url = "https://api-inference.huggingface.com/pipeline/feature-extraction/sentence-transformers/all-MiniLM-L6-v2"

    headers = {"Authorization": f"Bearer {HF_TOKEN}"}

    payload = {
        "inputs": text,
        "options": {"wait_for_model": True}
    }

    async with httpx.AsyncClient(timeout=60) as client:
        response = await client.post(url, headers=headers, json=payload)

    if response.status_code != 200:
        raise Exception(f"Embedding error: {response.text}")

    return response.json()[0]
