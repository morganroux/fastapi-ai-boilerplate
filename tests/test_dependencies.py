import pytest
from unittest.mock import Mock
from fastapi.testclient import TestClient
from dependencies import get_user_service, get_order_service
from services.user_service import UserService
from services.order_service import OrderService
from main import app

def test_dependency_override():
    """Test overriding dependencies for testing"""
    mock_user_service = Mock(spec=UserService)
    mock_user_service.get_all_users.return_value = [
        {"id": 1, "username": "testuser", "email": "test@example.com"}
    ]
    
    app.dependency_overrides[get_user_service] = lambda: mock_user_service
    
    client = TestClient(app)
    response = client.get("/users/")
    
    assert response.status_code == 200
    mock_user_service.get_all_users.assert_called_once()
    
    app.dependency_overrides.clear()

def test_multiple_dependencies():
    """Test endpoint using multiple dependencies"""
    mock_user_service = Mock(spec=UserService)
    mock_order_service = Mock(spec=OrderService)
    
    mock_user_service.get_all_users.return_value = []
    mock_order_service.get_user_orders.return_value = []
    
    app.dependency_overrides[get_user_service] = lambda: mock_user_service
    app.dependency_overrides[get_order_service] = lambda: mock_order_service
    
    client = TestClient(app)
    response = client.get("/admin/stats/")
    
    assert response.status_code == 200
    assert response.json() == {
        "total_users": 0,
        "total_orders": 0,
        "total_revenue": 0
    }
    
    app.dependency_overrides.clear()