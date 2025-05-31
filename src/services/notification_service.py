from abc import ABC, abstractmethod
from typing import List, Optional
from src.repository.notification_repository import NotificationRepositoryInterface
from src.repository.user_repository import UserRepositoryInterface
from src.providers.message_provider import MessageProviderInterface
from src.models.models import Notification, NotificationCreate

class NotificationServiceInterface(ABC):
    @abstractmethod
    def create_notification(self, notification_data: NotificationCreate, send_message: bool = True) -> Notification:
        pass

    @abstractmethod
    def get_notification(self, notification_id: int) -> Optional[Notification]:
        pass

    @abstractmethod
    def get_user_notifications(self, user_id: int) -> List[Notification]:
        pass

    @abstractmethod
    def mark_as_read(self, notification_id: int) -> Optional[Notification]:
        pass

    @abstractmethod
    def send_notification_message(self, notification: Notification) -> dict:
        pass

class NotificationService(NotificationServiceInterface):
    def __init__(self, 
                 notification_repository: NotificationRepositoryInterface,
                 user_repository: UserRepositoryInterface,
                 message_provider: MessageProviderInterface):
        self.notification_repository = notification_repository
        self.user_repository = user_repository
        self.message_provider = message_provider

    def create_notification(self, notification_data: NotificationCreate, send_message: bool = True) -> Notification:
        user = self.user_repository.get_user_by_id(notification_data.user_id)
        if not user:
            raise ValueError(f"User with ID {notification_data.user_id} not found")

        db_notification = self.notification_repository.create_notification(notification_data)
        notification = Notification.from_orm(db_notification)
        
        if send_message:
            self.send_notification_message(notification)
        
        return notification

    def get_notification(self, notification_id: int) -> Optional[Notification]:
        db_notification = self.notification_repository.get_notification_by_id(notification_id)
        return Notification.from_orm(db_notification) if db_notification else None

    def get_user_notifications(self, user_id: int) -> List[Notification]:
        db_notifications = self.notification_repository.get_notifications_by_user(user_id)
        return [Notification.from_orm(notification) for notification in db_notifications]

    def mark_as_read(self, notification_id: int) -> Optional[Notification]:
        db_notification = self.notification_repository.update_notification_status(notification_id, "read")
        return Notification.from_orm(db_notification) if db_notification else None

    def send_notification_message(self, notification: Notification) -> dict:
        user = self.user_repository.get_user_by_id(notification.user_id)
        if not user:
            raise ValueError(f"User with ID {notification.user_id} not found")
        
        return self.message_provider.send_message(
            recipient=user.email,
            title=notification.title,
            message=notification.message,
            message_type=notification.notification_type
        )