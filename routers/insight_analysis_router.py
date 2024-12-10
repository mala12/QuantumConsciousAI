from fastapi import APIRouter

router = APIRouter()

@router.get("/insight-analysis")
def insight_analysis_route():
    return {"message": "This is the insight analysis router"}
