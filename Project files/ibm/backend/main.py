# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from chat_router import router as chat_router
# from vector_router import router as vector_router
# from kpi_upload_router import router as kpi_upload_router
# from feedback_router import router as feedback_router

# app = FastAPI(title="Sustainable Smartcity Assistant API")

# # Allow CORS for local frontend
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # For production, restrict this
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# app.include_router(chat_router)
# app.include_router(vector_router)
# app.include_router(kpi_upload_router)
# app.include_router(feedback_router)

# @app.get("/")
# def root():
#     return {"message": "Sustainable Smartcity Assistant API is running."} 


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from chat_router import router as chat_router
from vector_router import router as vector_router
from kpi_upload_router import router as kpi_upload_router
from feedback_router import router as feedback_router

app = FastAPI(title="Sustainable Smart City Assistant API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat_router)
app.include_router(vector_router)
app.include_router(kpi_upload_router)
app.include_router(feedback_router)

@app.get("/")
def root():
    return {"message": "Sustainable Smart City Assistant API is running 🚀"}
