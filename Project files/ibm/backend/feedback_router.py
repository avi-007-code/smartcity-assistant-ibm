from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/feedback", tags=["Citizen Feedback"])

feedback_store = []

class Feedback(BaseModel):
    name: str
    category: str
    message: str

@router.post("/submit")
def submit_feedback(feedback: Feedback):
    feedback_store.append(feedback.dict())
    return {"message": "Feedback submitted successfully"}

@router.get("/all")
def get_all_feedback():
    return {"feedback": feedback_store}
