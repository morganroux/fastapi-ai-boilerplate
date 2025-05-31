from fastapi import APIRouter, HTTPException, Depends
from typing import List
from src.container.dependencies import get_notification_service
from src.services.notification_service import NotificationService
from src.models.models import Notification, NotificationCreate

router = APIRouter(prefix="/notifications", tags=["notifications"])

@router.post("/", response_model=Notification)
def create_notification(
    notification_data: NotificationCreate,
    notification_service: NotificationService = Depends(get_notification_service)
):
    """Create a new notification and send it"""
    try:
        return notification_service.create_notification(notification_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{notification_id}", response_model=Notification)
def get_notification(
    notification_id: int,
    notification_service: NotificationService = Depends(get_notification_service)
):
    """Get notification by ID"""
    notification = notification_service.get_notification(notification_id)
    if not notification:
        raise HTTPException(status_code=404, detail="Notification not found")
    return notification

@router.get("/user/{user_id}", response_model=List[Notification])
def get_user_notifications(
    user_id: int,
    notification_service: NotificationService = Depends(get_notification_service)
):
    """Get all notifications for a user"""
    return notification_service.get_user_notifications(user_id)

@router.put("/{notification_id}/read", response_model=Notification)
def mark_notification_as_read(
    notification_id: int,
    notification_service: NotificationService = Depends(get_notification_service)
):
    """Mark a notification as read"""
    notification = notification_service.mark_as_read(notification_id)
    if not notification:
        raise HTTPException(status_code=404, detail="Notification not found")
    return notification

@router.post("/{notification_id}/resend")
def resend_notification(
    notification_id: int,
    notification_service: NotificationService = Depends(get_notification_service)
):
    """Resend a notification message"""
    notification = notification_service.get_notification(notification_id)
    if not notification:
        raise HTTPException(status_code=404, detail="Notification not found")
    
    try:
        result = notification_service.send_notification_message(notification)
        return {"message": "Notification resent successfully", "result": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))