from fastapi import APIRouter

router = APIRouter()

@router.get("/auth")
def auth_route():
    return {"message": "This is the auth router"}

