from fastapi import APIRouter, Depends
from typing import List
from src.container.dependencies import get_user_service, get_order_service
from src.services.user_service import UserService
from src.services.order_service import OrderService
from src.models.models import User, Order

router = APIRouter(prefix="/admin", tags=["admin"])

@router.get("/users/", response_model=List[User])
def admin_get_all_users(
    user_service: UserService = Depends(get_user_service)
):
    """Admin endpoint to get all users"""
    return user_service.get_all_users()

@router.get("/stats/")
def admin_get_stats(
    user_service: UserService = Depends(get_user_service),
    order_service: OrderService = Depends(get_order_service)
):
    """Admin endpoint to get system stats"""
    users = user_service.get_all_users()

    all_orders = []
    for user in users:
        orders = order_service.get_user_orders(user.id)
        all_orders.extend(orders)

    return {
        "total_users": len(users),
        "total_orders": len(all_orders),
        "total_revenue": sum(order.total_amount for order in all_orders)
    }
