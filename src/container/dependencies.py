from typing import Generator
from src.container.container import get_container
from src.services.user_service import UserService
from src.services.order_service import OrderService
from src.services.notification_service import NotificationService
from src.repository.user_repository import UserRepository
from src.repository.order_repository import OrderRepository
from src.repository.notification_repository import NotificationRepository
from src.db.database import DatabaseConnection

def get_user_service() -> UserService:
    """FastAPI dependency for UserService"""
    return get_container().get_user_service()

def get_order_service() -> OrderService:
    """FastAPI dependency for OrderService"""
    return get_container().get_order_service()

def get_user_repository() -> UserRepository:
    """FastAPI dependency for UserRepository"""
    return get_container().get_user_repository()

def get_order_repository() -> OrderRepository:
    """FastAPI dependency for OrderRepository"""
    return get_container().get_order_repository()

def get_notification_service() -> NotificationService:
    """FastAPI dependency for NotificationService"""
    return get_container().get_notification_service()

def get_notification_repository() -> NotificationRepository:
    """FastAPI dependency for NotificationRepository"""
    return get_container().get_notification_repository()

def get_database_connection() -> DatabaseConnection:
    """FastAPI dependency for DatabaseConnection"""
    return get_container().get_database_connection()

def get_db_session() -> Generator:
    """FastAPI dependency for database session"""
    db_connection = get_container().get_database_connection()
    with db_connection.get_session() as session:
        yield session
