from pydantic import BaseModel

class OrderCreate(BaseModel):
    customer_name: str
    product: str
    quantity: int

class OrderStatusUpdate(BaseModel):
    status: str  # Only PENDING → SHIPPED → DELIVERED allowed