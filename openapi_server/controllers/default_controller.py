import connexion


from openapi_server.models.product_price import ProductPrice  # noqa: E501
from openapi_server.services.service import DealService


deal_service = DealService()


def add_product_price():  # noqa: E501
    """receive a new product price from a participating retailer

     # noqa: E501

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        product_price = ProductPrice.from_dict(connexion.request.get_json())  # noqa: E501
        deal_service.add_deal(product_price)

        return None, 201
    return None, 400


def search_for_product_price(sku=None):  # noqa: E501
    product_price = deal_service.find_deal(sku)
    if not product_price:
        return None, 404
    return product_price
