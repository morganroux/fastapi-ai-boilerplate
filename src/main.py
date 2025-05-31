from fastapi import FastAPI
from src.container.container import get_container
from src.routes import users, orders, admin, notifications

def create_app() -> FastAPI:
    app = FastAPI(title="E-commerce API with Centralized Dependencies")

    container = get_container()
    db_connection = container.get_database_connection()
    db_connection.create_tables()

    app.include_router(users.router)
    app.include_router(orders.router)
    app.include_router(admin.router)
    app.include_router(notifications.router)

    return app

app = create_app()

@app.get("/")
def root():
    return {"message": "E-commerce API with centralized dependencies"}
