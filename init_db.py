from app.db.database import engine, Base
from app.models.order import Order

Base.metadata.create_all(bind=engine)