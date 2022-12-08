from fastapi import HTTPException, status
from database.config import DBConnectionHandler
from ..entities import orders
from ..models.create_order import OrderSchemaPost 
import datetime
from base_app.utils.func import number_order


class OrdersRepository:
     """ class to manage product repo """
     @classmethod
     def read_all_orders(cls):
        with DBConnectionHandler() as db_connection:
            try:

                all_orders = db_connection.session.query(
                orders.Orders.numero_pedido,
                orders.Orders.data_criacao,
                orders.Orders.status_pedido,
                orders.Orders.preco_pedido
                )\
                .all()

                return all_orders

            finally:
                db_connection.session.close()
                
     @classmethod
     def create_order(cls, order: OrderSchemaPost):
        with DBConnectionHandler() as db_connection:
            try:

                create = orders.Orders()
                create.ativo = True
                create.data_criacao = datetime.datetime.now()
                create.data_modificacao = datetime.datetime.now()
                create.numero_pedido = number_order(5)
                create.status_pedido = 1
                create.preco_pedido = order.preco_pedido
                create.fk_UUID_usuario_id = order.fk_UUID_usuario_id

                db_connection.session.add(create)
                db_connection.session.commit()

            finally:
                return HTTPException(status_code=status.HTTP_202_ACCEPTED, detail="User created")