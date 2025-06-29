import os
from dotenv import load_dotenv
import httpx

load_dotenv()

IBM_API_KEY = os.getenv("IBM_API_KEY")
IBM_PROJECT_ID = os.getenv("IBM_PROJECT_ID")  # From your watsonx.ai project
IBM_REGION = "us-south"  # or "eu-de" depending on your instance

async def get_ibm_access_token() -> str:
    """Get IAM token using IBM API key."""
    async with httpx.AsyncClient() as client:
        res = await client.post(
            "https://iam.cloud.ibm.com/identity/token",
            data={
                "grant_type": "urn:ibm:params:oauth:grant-type:apikey",
                "apikey": IBM_API_KEY,
            },
            headers={"Content-Type": "application/x-www-form-urlencoded"},
        )
        if res.status_code != 200:
            raise Exception(f"IBM Auth error: {res.text}")
        return res.json()["access_token"]

async def ask_granite_llm(prompt: str) -> str:
    """Call IBM watsonx Granite model with a prompt."""
    token = await get_ibm_access_token()

    url = f"https://{IBM_REGION}.ml.cloud.ibm.com/ml/v1/text/generation"

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "X-Watson-Project-Id": IBM_PROJECT_ID,
    }

    payload = {
        "model_id": "ibm/granite-3b-instruct",  # or granite-3.3-2b-instruct if enabled
        "input": prompt,
        "parameters": {
            "decoding_method": "greedy",
            "max_new_tokens": 300,
            "temperature": 0.7,
        }
    }

    async with httpx.AsyncClient(timeout=60) as client:
        response = await client.post(url, headers=headers, json=payload)

    if response.status_code != 200:
        raise Exception(f"LLM error: {response.text}")

    result = response.json()
    return result["results"][0]["generated_text"]
