from .repo.query_products import ProductsRepository
from .models.post_product import ProductSchema

class GetAllProducts():
    
    def execute():
        products = ProductsRepository.get_products()
        return products

class PostProduct():
    
    def execute(produto: ProductSchema):
        products = ProductsRepository.insert_product(produto)
        return products
    