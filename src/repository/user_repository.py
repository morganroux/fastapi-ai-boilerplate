from abc import ABC, abstractmethod
from typing import List, Optional
from sqlalchemy.orm import Session
from src.models.models import UserModel, User, UserCreate
from src.db.database import DatabaseConnection

class UserRepositoryInterface(ABC):
    @abstractmethod
    def create_user(self, user_data: UserCreate) -> UserModel:
        pass

    @abstractmethod
    def get_user_by_id(self, user_id: int) -> Optional[UserModel]:
        pass

    @abstractmethod
    def get_all_users(self) -> List[UserModel]:
        pass

    @abstractmethod
    def delete_user(self, user_id: int) -> bool:
        pass

class UserRepository(UserRepositoryInterface):
    def __init__(self, db_connection: DatabaseConnection):
        self.db_connection = db_connection

    def create_user(self, user_data: UserCreate) -> UserModel:
        with self.db_connection.get_session() as session:
            db_user = UserModel(**user_data.dict())
            session.add(db_user)
            session.flush()
            session.refresh(db_user)
            return db_user

    def get_user_by_id(self, user_id: int) -> Optional[UserModel]:
        with self.db_connection.get_session() as session:
            return session.query(UserModel).filter(UserModel.id == user_id).first()

    def get_all_users(self) -> List[UserModel]:
        with self.db_connection.get_session() as session:
            return session.query(UserModel).all()

    def delete_user(self, user_id: int) -> bool:
        with self.db_connection.get_session() as session:
            user = session.query(UserModel).filter(UserModel.id == user_id).first()
            if user:
                session.delete(user)
                return True
            return False
