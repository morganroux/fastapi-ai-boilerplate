import os
from typing import Optional
from src.db.database import DatabaseConnection
from src.repository.user_repository import UserRepository
from src.repository.order_repository import OrderRepository
from src.services.user_service import UserService
from src.services.order_service import OrderService

class DIContainer:
    def __init__(self, database_url: str):
        self._database_url = database_url
        self._database_connection: Optional[DatabaseConnection] = None
        self._user_repository: Optional[UserRepository] = None
        self._order_repository: Optional[OrderRepository] = None
        self._user_service: Optional[UserService] = None
        self._order_service: Optional[OrderService] = None

    def get_database_connection(self) -> DatabaseConnection:
        if self._database_connection is None:
            self._database_connection = DatabaseConnection(self._database_url)
        return self._database_connection

    def get_user_repository(self) -> UserRepository:
        if self._user_repository is None:
            self._user_repository = UserRepository(self.get_database_connection())
        return self._user_repository

    def get_order_repository(self) -> OrderRepository:
        if self._order_repository is None:
            self._order_repository = OrderRepository(self.get_database_connection())
        return self._order_repository

    def get_user_service(self) -> UserService:
        if self._user_service is None:
            self._user_service = UserService(self.get_user_repository())
        return self._user_service

    def get_order_service(self) -> OrderService:
        if self._order_service is None:
            self._order_service = OrderService(
                self.get_order_repository(),
                self.get_user_repository()
            )
        return self._order_service

# Global container
container: Optional[DIContainer] = None

def get_container() -> DIContainer:
    global container
    if container is None:
        database_url = os.getenv("DATABASE_URL", "sqlite:///./test.db")
        container = DIContainer(database_url)
    return container
