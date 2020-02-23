from unittest import TestCase
from flask import json
from api import api

class Tests(TestCase):
  def setUp(self):
        self.app = app
        self.client = self.app.test_client
 
  def test_get_specific_item(self):
        get_result = self.client().get('/product/<int:product_id>')
        self.assertEqual(get_result.status_code, 200)
        get_result1 = self.client().get('/product/laptop')
        self.assertEqual(get_result1.status_code, 404)
  def test_get_all_products(self):
        get_result = self.client().get('/products')
        self.assertEqual(get_result.status_code, 200)

  def test_add_product(self):
        post_result = self.client().post('/products', 
                                    data=json.dumps(dict(name="laptop",
                                    quantity= 42, price = 2000000, min_quantity = 10)))
        self.assertEqual(post_result.status_code, 201)   

        json_data = json.loads(post_result.data)      
        assert json_data['name'] == "laptop"
        assert json_data['quantity'] == 42
        assert json_data['unitPx'] == 2000000
        assert json_data['minQuantity'] == 10

  def test_get_specific_sale(self):
        get_result = self.client().get('/sale/<int:sale_id>')
        self.assertEqual(get_result.status_code, 200)
        get_result1 = self.client().get('/api/v1/sale/laptop')
        self.assertEqual(get_result1.status_code, 404)
  def test_get_all_sales(self):
        get_result = self.client().get('/sale')
        self.assertEqual(get_result.status_code, 200)

  def test_add_sale(self):
        post_result = self.client().post('/api/v1/sales', 
                                    data=json.dumps(dict(name = "laptop", quantity = 5, price = 10)))
        self.assertEqual(post_result.status_code, 201)                 
        

        

