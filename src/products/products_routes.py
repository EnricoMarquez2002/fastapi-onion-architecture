from fastapi import APIRouter
from .use_cases import GetAllProducts, PostProduct, UpdateProduct, DeleteProduct
from .models.post_product import ProductSchema
from .models.update_product import ProductSchemaUp


router = APIRouter(
    prefix='/products',
    tags= ["Products"]
)

@router.get('')
async def read_products():
    products = GetAllProducts.execute()
    return products

@router.post('')
async def create_product(produto: ProductSchema):
    product = PostProduct.execute(produto)
    return product

@router.patch('/{name}')
async def update_product(product_name: str, product: ProductSchemaUp):
    product_up = UpdateProduct.execute(product_name, product)
    return product_up

@router.delete('')
async def delete_product(product_id: str):
    product = DeleteProduct.execute(product_id)
    return product

