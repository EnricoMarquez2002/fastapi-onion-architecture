from fastapi import APIRouter
from .use_cases import GetAllProducts, PostProduct
from .models.post_product import ProductSchema


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
