from fastapi import HTTPException, status
from database.config import DBConnectionHandler
from entities import products
from models.post_product import ProductSchema
import datetime
import uuid


class ProductsRepository():
    """ class to manage product repo """
    
    @classmethod
    def get_products(cls):
        with DBConnectionHandler() as db_connection:
            try:
                all_products = db_connection.session.query(
                    products.Products.nome,
                    products.Products.preco,
                    products.Products.preco_atual,
                    products.Products.promocao
                )\
                .all()
                return all_products
            finally:
                db_connection.session.close()

    @classmethod
    def insert_product(cls, produto: ProductSchema):
        with DBConnectionHandler() as db_connection:
            try:

                create_product = products.Products()
                create_product.ativo = True
                create_product.data_criacao = datetime.datetime.now()
                create_product.data_modificacao = datetime.datetime.now()
                create_product.id_produto = uuid.uuid4
                create_product.nome = produto.nome
                create_product.preco = produto.preco
                create_product.preco_atual = produto.preco_atual
                create_product.promocao = produto.promocao

                db_connection.session.add(create_product)
                db_connection.session.commit()

            finally:
                db_connection.session.close()

            return HTTPException(status_code=status.HTTP_201_CREATED, detail="Product created")

            