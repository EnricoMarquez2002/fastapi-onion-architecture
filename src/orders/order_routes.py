from fastapi import APIRouter
from .use_cases import GetAllOrders, PostOrder
from orders.models.create_order import OrderSchemaPost


router = APIRouter(
    prefix= '/orders',
    tags= ["Orders"]
)

@router.get('')
async def read_all_orders():
    all_orders = GetAllOrders.execute()
    return all_orders

@router.post('')
async def create_order(order: OrderSchemaPost):
    create = PostOrder.execute(order)
    return create