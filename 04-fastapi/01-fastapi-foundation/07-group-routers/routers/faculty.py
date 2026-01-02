from fastapi import APIRouter
from utils import faculty_utility

router = APIRouter()

@router.get("/faculty-bio")
def faculty_bio():
    departments = faculty_utility.all_department()
    return {
        "status": 200,
        "data": {
            "departments": departments,
            "name": "Dr. Moiz Ali",
            "Field": "AI Researcher",
            "Experience": "7 years"

        }
    }