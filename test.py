import unittest

from openapi_server.models import ProductPrice
from openapi_server.services.service import DealService

test_sku = "foo-bar-baz"


def get_test_product_price(price) -> ProductPrice:
    product_price = ProductPrice()
    product_price.price = price
    product_price.sku = test_sku
    product_price.retailer = "my-retail-co"
    return product_price


class TestDealService(unittest.TestCase):
    def test_can_add_and_find_one_product_price(self):
        # given
        deal_service = DealService()
        deal_service.add_deal(get_test_product_price(1))

        # when
        product = deal_service.find_deal(test_sku)

        # then
        self.assertIsNotNone(product)
        self.assertEqual(product.sku, test_sku)

    def test_can_find_the_lowest_price(self):
        # given
        deal_service = DealService()
        deal_service.add_deal(get_test_product_price(3.7))
        deal_service.add_deal(get_test_product_price(9.1))
        deal_service.add_deal(get_test_product_price(10))

        # when
        product = deal_service.find_deal(test_sku)

        # then
        self.assertIsNotNone(product)
        self.assertEqual(product.price, 3.7)


if __name__ == '__main__':
    unittest.main()
