from fastapi import APIRouter, HTTPException, Depends
from typing import List
from src.container.dependencies import get_order_service, get_user_service
from src.services.order_service import OrderService
from src.services.user_service import UserService
from src.models.models import Order, OrderCreate

router = APIRouter(prefix="/orders", tags=["orders"])

@router.post("/", response_model=Order)
def create_order(
    order_data: OrderCreate,
    order_service: OrderService = Depends(get_order_service)
):
    """Create a new order"""
    try:
        return order_service.create_order(order_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{order_id}", response_model=Order)
def get_order(
    order_id: int,
    order_service: OrderService = Depends(get_order_service)
):
    """Get order by ID"""
    order = order_service.get_order(order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@router.get("/user/{user_id}", response_model=List[Order])
def get_user_orders(
    user_id: int,
    order_service: OrderService = Depends(get_order_service),
    user_service: UserService = Depends(get_user_service)
):
    """Get all orders for a user"""
    user = user_service.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return order_service.get_user_orders(user_id)
