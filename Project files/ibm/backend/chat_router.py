# from fastapi import APIRouter, Form, Request
# from fastapi.responses import JSONResponse
# from granite_llm import ask_granite_llm
# import asyncio

# router = APIRouter()

# @router.post("/chat")
# async def chat_endpoint(request: Request):
#     if request.headers.get("content-type", "").startswith("application/json"):
#         data = await request.json()
#         prompt = data.get("prompt", "")
#     else:
#         form = await request.form()
#         prompt = form.get("prompt", "")
#     response = await ask_granite_llm(prompt)
#     return JSONResponse({"response": response}) 


# from fastapi import APIRouter, HTTPException
# from pydantic import BaseModel
# from granite_llm import ask_granite_llm  # Import the function that calls IBM Granite LLM

# # Initialize router
# router = APIRouter(
#     prefix="/chat",
#     tags=["Chatbot"]
# )

# # Request body model
# class PromptRequest(BaseModel):
#     prompt: str

# # Response model (optional but recommended)
# class ChatResponse(BaseModel):
#     response: str


# # 🔥 Chat endpoint — send prompt to Granite LLM
# @router.post("/ask", response_model=ChatResponse)
# async def chat_with_granite(request: PromptRequest):
#     """
#     Send a prompt to Granite LLM and get a response.
#     """
#     try:
#         response = await ask_granite_llm(request.prompt)
#         return {"response": response}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Granite LLM error: {str(e)}")

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from granite_llm import ask_granite_llm  # ✅ Import the chatbot function

router = APIRouter(prefix="/chat", tags=["Chat Assistant"])

class PromptRequest(BaseModel):
    prompt: str

@router.post("/ask")
async def chat_with_assistant(request: PromptRequest):
    try:
        response = await ask_granite_llm(request.prompt)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

