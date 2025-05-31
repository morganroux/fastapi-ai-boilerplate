from abc import ABC, abstractmethod
from typing import List, Optional
from src.models.models import OrderModel, Order, OrderCreate
from src.db.database import DatabaseConnection

class OrderRepositoryInterface(ABC):
    @abstractmethod
    def create_order(self, order_data: OrderCreate) -> OrderModel:
        pass

    @abstractmethod
    def get_order_by_id(self, order_id: int) -> Optional[OrderModel]:
        pass

    @abstractmethod
    def get_orders_by_user(self, user_id: int) -> List[OrderModel]:
        pass

class OrderRepository(OrderRepositoryInterface):
    def __init__(self, db_connection: DatabaseConnection):
        self.db_connection = db_connection

    def create_order(self, order_data: OrderCreate) -> OrderModel:
        with self.db_connection.get_session() as session:
            db_order = OrderModel(**order_data.dict())
            session.add(db_order)
            session.flush()
            session.refresh(db_order)
            return db_order

    def get_order_by_id(self, order_id: int) -> Optional[OrderModel]:
        with self.db_connection.get_session() as session:
            return session.query(OrderModel).filter(OrderModel.id == order_id).first()

    def get_orders_by_user(self, user_id: int) -> List[OrderModel]:
        with self.db_connection.get_session() as session:
            return session.query(OrderModel).filter(OrderModel.user_id == user_id).all()
