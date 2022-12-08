from .repo.orders_repo import OrdersRepository
from orders.models.create_order import OrderSchemaPost 

class GetAllOrders():

    def execute():
        all_orders = OrdersRepository.read_all_orders()
        return all_orders
        
class PostOrder():

    def execute(order: OrderSchemaPost):
        create = OrdersRepository.create_order(order)
        return create