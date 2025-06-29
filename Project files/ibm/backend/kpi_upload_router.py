# from fastapi import APIRouter, UploadFile, File
# from fastapi.responses import JSONResponse
# import pandas as pd
# from kpi_file_forecaster import summarize_file, detect_anomalies

# router = APIRouter()

# @router.post("/upload")
# async def upload_kpi_file(file: UploadFile = File(...)):
#     content = await file.read()
#     filename = file.filename.lower()
#     summary = ""
#     anomalies = []
#     if filename.endswith(".csv"):
#         try:
#             df = pd.read_csv(pd.compat.StringIO(content.decode()))
#             summary = summarize_file(content.decode())
#             anomaly_indices = detect_anomalies(df)
#             if anomaly_indices:
#                 anomalies = df.iloc[anomaly_indices].to_dict(orient="records")
#         except Exception as e:
#             return JSONResponse({"error": f"Failed to process CSV: {e}"}, status_code=400)
#     elif filename.endswith(".txt"):
#         summary = summarize_file(content.decode())
#     else:
#         return JSONResponse({"error": "Unsupported file type."}, status_code=400)
#     return JSONResponse({"summary": summary, "anomalies": anomalies}) 

from fastapi import APIRouter, UploadFile, File, HTTPException
from pydantic import BaseModel
import aiofiles
import os
from transformers import pipeline

# Initialize Hugging Face summarization pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

router = APIRouter(prefix="/kpi", tags=["KPI Upload & Summary"])

# ✅ Text-based summarization
class TextInput(BaseModel):
    text: str


@router.post("/summarize")
async def summarize_text(input: TextInput):
    try:
        summary = summarizer(input.text, max_length=200, min_length=30, do_sample=False)
        return {"summary": summary[0]['summary_text']}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Summarization error: {e}")


# ✅ File upload summarization (supports txt and pdf)
@router.post("/upload")
async def upload_and_summarize(file: UploadFile = File(...)):
    try:
        if file.content_type not in ["text/plain", "application/pdf"]:
            raise HTTPException(status_code=400, detail="Only .txt or .pdf files are supported.")

        file_location = f"temp_files/{file.filename}"
        os.makedirs("temp_files", exist_ok=True)

        # Save the uploaded file
        async with aiofiles.open(file_location, 'wb') as out_file:
            content = await file.read()
            await out_file.write(content)

        # Read file content
        if file.content_type == "text/plain":
            async with aiofiles.open(file_location, 'r', encoding='utf-8') as f:
                text = await f.read()

        elif file.content_type == "application/pdf":
            import PyPDF2
            with open(file_location, 'rb') as f:
                reader = PyPDF2.PdfReader(f)
                text = ""
                for page in reader.pages:
                    text += page.extract_text() or ""

        if not text.strip():
            raise HTTPException(status_code=400, detail="No readable content in file.")

        # Summarize
        summary = summarizer(text, max_length=200, min_length=30, do_sample=False)

        return {
            "filename": file.filename,
            "summary": summary[0]['summary_text']
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"File summarization error: {e}")
    finally:
        # Clean up temp file
        if os.path.exists(file_location):
            os.remove(file_location)
