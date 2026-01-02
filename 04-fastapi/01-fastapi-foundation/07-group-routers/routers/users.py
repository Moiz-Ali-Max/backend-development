from fastapi import APIRouter

router = APIRouter()

@router.get("/user-bio")
def user_bio():
    return {
        "status": 200,
        "data": {
            "name": "Moiz Ali",
            "field": " AI Engineer",
            "Location": "Islamabad",
            "University": "SZBIST"
        }
    }