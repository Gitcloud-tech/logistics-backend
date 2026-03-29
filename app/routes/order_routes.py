from fastapi import APIRouter
from app.schemas.order_schema import OrderCreate
from app.services.order_service import create_order, get_orders, update_order_status

router = APIRouter()

@router.post("/orders")
def create(order: OrderCreate):
    return create_order(order)

@router.get("/orders")
def list_orders():
    return get_orders()

@router.put("/orders/{order_id}/status")
def change_status(order_id: int):
    return update_order_status(order_id)