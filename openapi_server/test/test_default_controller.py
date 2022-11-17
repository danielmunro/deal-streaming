# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.product_price import ProductPrice  # noqa: E501
from openapi_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_add_product_price(self):
        """Test case for add_product_price

        receive a new product price from a participating retailer
        """
        product_price = {"retailer":"retailer","price":0.8008281904610115,"sku":"sku","url":"url"}
        headers = { 
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/product-price',
            method='POST',
            headers=headers,
            data=json.dumps(product_price),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_search_for_product_price(self):
        """Test case for search_for_product_price

        search for a product price via an SKU
        """
        query_string = [('sku', 'sku_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/product-price',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
