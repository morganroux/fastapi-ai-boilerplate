from abc import ABC, abstractmethod
from typing import List, Optional
from src.repository.order_repository import OrderRepositoryInterface
from src.repository.user_repository import UserRepositoryInterface
from src.models.models import Order, OrderCreate

class OrderServiceInterface(ABC):
    @abstractmethod
    def create_order(self, order_data: OrderCreate) -> Order:
        pass

    @abstractmethod
    def get_order(self, order_id: int) -> Optional[Order]:
        pass

    @abstractmethod
    def get_user_orders(self, user_id: int) -> List[Order]:
        pass

class OrderService(OrderServiceInterface):
    def __init__(self, order_repository: OrderRepositoryInterface, user_repository: UserRepositoryInterface):
        self.order_repository = order_repository
        self.user_repository = user_repository

    def create_order(self, order_data: OrderCreate) -> Order:
        user = self.user_repository.get_user_by_id(order_data.user_id)
        if not user:
            raise ValueError(f"User with ID {order_data.user_id} not found")

        db_order = self.order_repository.create_order(order_data)
        return Order.from_orm(db_order)

    def get_order(self, order_id: int) -> Optional[Order]:
        db_order = self.order_repository.get_order_by_id(order_id)
        return Order.from_orm(db_order) if db_order else None

    def get_user_orders(self, user_id: int) -> List[Order]:
        db_orders = self.order_repository.get_orders_by_user(user_id)
        return [Order.from_orm(order) for order in db_orders]
