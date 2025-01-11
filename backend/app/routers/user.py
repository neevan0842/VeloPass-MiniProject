from fastapi import APIRouter, Depends

from ..auth.auth_handler import get_current_active_user
from ..schemas import UserResponse
from ..models import User

router = APIRouter()


@router.get("/me", response_model=UserResponse)
async def get_current_user(current_user: User = Depends(get_current_active_user)):
    return current_user