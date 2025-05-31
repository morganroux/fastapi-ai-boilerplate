from abc import ABC, abstractmethod
from typing import List, Optional
from src.repository.user_repository import UserRepositoryInterface
from src.models.models import User, UserCreate

class UserServiceInterface(ABC):
    @abstractmethod
    def create_user(self, user_data: UserCreate) -> User:
        pass

    @abstractmethod
    def get_user(self, user_id: int) -> Optional[User]:
        pass

    @abstractmethod
    def get_all_users(self) -> List[User]:
        pass

class UserService(UserServiceInterface):
    def __init__(self, user_repository: UserRepositoryInterface):
        self.user_repository = user_repository

    def create_user(self, user_data: UserCreate) -> User:
        db_user = self.user_repository.create_user(user_data)
        return User.from_orm(db_user)

    def get_user(self, user_id: int) -> Optional[User]:
        db_user = self.user_repository.get_user_by_id(user_id)
        return User.from_orm(db_user) if db_user else None

    def get_all_users(self) -> List[User]:
        db_users = self.user_repository.get_all_users()
        return [User.from_orm(user) for user in db_users]
