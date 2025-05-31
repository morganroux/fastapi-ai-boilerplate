from fastapi import APIRouter, HTTPException, Depends
from typing import List
from src.container.dependencies import get_user_service
from src.services.user_service import UserService
from src.models.models import User, UserCreate

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=User)
def create_user(
    user_data: UserCreate,
    user_service: UserService = Depends(get_user_service)
):
    """Create a new user"""
    try:
        return user_service.create_user(user_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{user_id}", response_model=User)
def get_user(
    user_id: int,
    user_service: UserService = Depends(get_user_service)
):
    """Get user by ID"""
    user = user_service.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get("/", response_model=List[User])
def get_users(
    user_service: UserService = Depends(get_user_service)
):
    """Get all users"""
    return user_service.get_all_users()
