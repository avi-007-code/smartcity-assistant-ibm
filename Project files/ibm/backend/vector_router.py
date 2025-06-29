# from fastapi import APIRouter, Form, Request
# from fastapi.responses import JSONResponse
# from pinecone_connection import get_index

# router = APIRouter()

# @router.post("/vector-search")
# async def vector_search(request: Request):
#     if request.headers.get("content-type", "").startswith("application/json"):
#         data = await request.json()
#         query = data.get("query", "")
#     else:
#         form = await request.form()
#         query = form.get("query", "")
#     # TODO: Embed query and search Pinecone
#     # For now, return mock result
#     return JSONResponse({"results": [f"Mock result for: {query}"]})

# @router.post("/search-tips")
# async def search_tips(request: Request):
#     if request.headers.get("content-type", "").startswith("application/json"):
#         data = await request.json()
#         keyword = data.get("keyword", "")
#     else:
#         form = await request.form()
#         keyword = form.get("keyword", "")
#     # TODO: Embed keyword and search Pinecone for eco tips
#     # For now, return mock tips
#     return JSONResponse({"tips": [f"Eco tip for: {keyword}", "Save water by fixing leaks.", "Use public transport."]}) 

# from fastapi import APIRouter, HTTPException
# from pydantic import BaseModel
# from pinecone_connection import get_index  # Function that returns the Pinecone index instance
# from embedding import get_embedding     # Function to generate embeddings (you can use Granite, HuggingFace, etc.)

# # Initialize Router
# router = APIRouter(
#     prefix="/vector",
#     tags=["Vector Search"]
# )

# # Request models
# class UpsertRequest(BaseModel):
#     id: str
#     text: str

# class QueryRequest(BaseModel):
#     query: str
#     top_k: int = 5


# # 🔥 Upsert Endpoint — Save text in Pinecone
# @router.post("/upsert")
# async def upsert_vector(item: UpsertRequest):
#     try:
#         index = get_index()
#         embedding = await get_embedding(item.text)

#         index.upsert([
#             {
#                 "id": item.id,
#                 "values": embedding,
#                 "metadata": {"text": item.text}
#             }
#         ])

#         return {"message": f"Item '{item.id}' upserted successfully."}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))


# # 🔍 Query Endpoint — Search for similar items
# @router.post("/query")
# async def query_vector(item: QueryRequest):
#     try:
#         index = get_index()
#         embedding = await get_embedding(item.query)

#         result = index.query(
#             vector=embedding,
#             top_k=item.top_k,
#             include_metadata=True
#         )

#         matches = [
#             {
#                 "id": m["id"],
#                 "score": m["score"],
#                 "text": m["metadata"].get("text")
#             }
#             for m in result.get("matches", [])
#         ]

#         return {"matches": matches}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from embedding_model import get_embedding
from pinecone_connection import get_index

router = APIRouter(prefix="/vector", tags=["Vector Database"])

index = get_index()

class TextItem(BaseModel):
    id: str
    text: str

@router.post("/upsert")
async def upsert_vector(item: TextItem):
    try:
        embedding = await get_embedding(item.text)
        index.upsert([(item.id, embedding)])
        return {"message": "Upsert successful"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/query")
async def query_vector(item: TextItem):
    try:
        embedding = await get_embedding(item.text)
        results = index.query(vector=embedding, top_k=5, include_metadata=True)
        return {"results": results.to_dict()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
