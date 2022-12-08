from .base_order import OrdersSchema


class OrderSchemaPost(OrdersSchema):
    fk_UUID_usuario_id: str

    class Config:
        schema_extra = {
            "example": {
                "preco_pedido": 0,
                "fk_UUID_usuario_id": "uuid"
            }
        }