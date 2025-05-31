from abc import ABC, abstractmethod
from typing import List, Optional
from src.models.models import NotificationModel, Notification, NotificationCreate
from src.db.database import DatabaseConnection

class NotificationRepositoryInterface(ABC):
    @abstractmethod
    def create_notification(self, notification_data: NotificationCreate) -> NotificationModel:
        pass

    @abstractmethod
    def get_notification_by_id(self, notification_id: int) -> Optional[NotificationModel]:
        pass

    @abstractmethod
    def get_notifications_by_user(self, user_id: int) -> List[NotificationModel]:
        pass

    @abstractmethod
    def update_notification_status(self, notification_id: int, status: str) -> Optional[NotificationModel]:
        pass

    @abstractmethod
    def delete_notification(self, notification_id: int) -> bool:
        pass

class NotificationRepository(NotificationRepositoryInterface):
    def __init__(self, db_connection: DatabaseConnection):
        self.db_connection = db_connection

    def create_notification(self, notification_data: NotificationCreate) -> NotificationModel:
        with self.db_connection.get_session() as session:
            db_notification = NotificationModel(**notification_data.dict())
            session.add(db_notification)
            session.flush()
            session.refresh(db_notification)
            return db_notification

    def get_notification_by_id(self, notification_id: int) -> Optional[NotificationModel]:
        with self.db_connection.get_session() as session:
            return session.query(NotificationModel).filter(NotificationModel.id == notification_id).first()

    def get_notifications_by_user(self, user_id: int) -> List[NotificationModel]:
        with self.db_connection.get_session() as session:
            return session.query(NotificationModel).filter(NotificationModel.user_id == user_id).order_by(NotificationModel.created_at.desc()).all()

    def update_notification_status(self, notification_id: int, status: str) -> Optional[NotificationModel]:
        with self.db_connection.get_session() as session:
            notification = session.query(NotificationModel).filter(NotificationModel.id == notification_id).first()
            if notification:
                notification.status = status
                session.flush()
                session.refresh(notification)
                return notification
            return None

    def delete_notification(self, notification_id: int) -> bool:
        with self.db_connection.get_session() as session:
            notification = session.query(NotificationModel).filter(NotificationModel.id == notification_id).first()
            if notification:
                session.delete(notification)
                return True
            return False