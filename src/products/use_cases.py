from .repo.query_products import ProductsRepository
from .models.post_product import ProductSchema
from .models.update_product import ProductSchemaUp
import datetime


class GetAllProducts():
    
    def execute():
        products = ProductsRepository.get_products()
        return products

class PostProduct():
    
    def execute(produto: ProductSchema):
        products = ProductsRepository.insert_product(produto)
        return products
    
class UpdateProduct():

    def execute(product_name: str, product: ProductSchemaUp):
        product_info = product.dict(exclude_unset=True)
        product_info["data_modificacao"] = datetime.datetime.now()

        product_up = ProductsRepository.update_product(product_name, product_info)
        return product_up



