import unittest

from openapi_server.models import ProductPrice
from openapi_server.services.service import DealService

test_sku = "foo-bar-baz"


def get_test_product_price() -> ProductPrice:
    product_price = ProductPrice()
    product_price.price = 1
    product_price.sku = test_sku
    product_price.retailer = "my-retail-co"
    return product_price


class TestDealService(unittest.TestCase):
    def test_can_add_and_find_one_product_price(self):
        # given
        deal_service = DealService()
        deal_service.add_deal(get_test_product_price())

        # when
        product = deal_service.find_deal(test_sku)

        # then
        self.assertIsNotNone(product)
        self.assertEqual(product.sku, test_sku)


if __name__ == '__main__':
    unittest.main()
