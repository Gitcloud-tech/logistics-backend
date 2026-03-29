from app.models.order import Order
from app.db.database import SessionLocal

# Allowed status transitions
STATUS_FLOW = {
    "PENDING": "SHIPPED",
    "SHIPPED": "DELIVERED",
    "DELIVERED": None
}

def create_order(order):
    db = SessionLocal()
    new_order = Order(
        customer_name=order.customer_name,
        product=order.product,
        quantity=order.quantity,
        status="PENDING"
    )
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    db.close()
    return new_order

def get_orders():
    db = SessionLocal()
    orders = db.query(Order).all()
    db.close()
    return orders

def update_order_status(order_id):
    db = SessionLocal()
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        db.close()
        return {"error": "Order not found"}
    
    next_status = STATUS_FLOW.get(order.status)
    if not next_status:
        db.close()
        return {"error": f"Cannot change status from {order.status}"}
    
    order.status = next_status
    db.commit()
    db.refresh(order)
    db.close()
    return order