#!/usr/bin/python3
"""
"""
from flask import Flask
from flask_restful import Api, Resource, reqparse


app = Flask(__name__)
api = Api(app)


companies = [
    {
        "company_id": 1,
        "name": "Coca-Cola"
    }
]

products = [
    {
        "product_id": 1,
        "name": "laptop",
        "quantity": 42,
        "min_quantity": 10,
        "unit_price": 2000000,
        "company_id": 1
    },
    {
        "product_id": 2,
        "name": "camera",
        "quantity": 75,
        "min_quantity": 30,
        "unit_price": 800000,
        "company_id": 1
    },
    {
        "product_id": 3,
        "name": "flat iron",
        "quantity": 84,
        "min_quantity": 45,
        "unit_price": 300000,
        "company_id": 1
    }
]


class CompanyProductList(Resource):
    def get(self, company_id):
        companies_products = []
        for product in products:
            if(company_id == product['company_id']):
                companies_products.append(product)
        return companies_products, 200


class CompanyList(Resource):
    def get(self):
        return companies


class CompanyProduct(Resource):
    def get(self, company_id, product_id):
        for product in products:
            if (company_id == product['company_id'] and
               product_id == product['product_id']):
                return product
        return "product not found", 404

    def post(self, company_id, product_id):
        parser = reqparse.RequestParser()
        parser.add_argument("name")
        parser.add_argument("quantity")
        parser.add_argument("min_quantity")
        parser.add_argument("unit_price")
        args = parser.parse_args()

        product = {
            "product_id": products[:-1]['product_id'],
            "name": args["name"],
            "quantity": args["quantity"],
            "min_quantity": args["min_quantity"],
            "unit_price": args["unit_price"],
            "company_id": company_id
        }
        products.append(product)
        return product, 201

    def put(self, product_id):
        parser = reqparse.RequestParser()
        parser.add_argument("name")
        parser.add_argument("quantity")
        parser.add_argument("min_quantity")
        parser.add_argument("unit_price")
        args = parser.parse_args()

        for product in products:
            if(product_id == product["product_id"]):
                product["name"] = args["name"]
                product["quantity"] = args["quantity"]
                product["min_quantity"] = args["min_quantity"]
                product["unit_price"] = args["unit_price"]
                return product, 200

        product = {
            "product_id": product_id,
            "name": args["name"],
            "quantity": args["quantity"],
            "min_quantity": args["min_quantity"],
            "unit_price": args["unit_price"]
        }
        products.append(product)
        return product, 201

    def delete(self, company_id, product_id):
        global products
        products = [product for product in products
                    if product["product_id"] != product_id]
        return "{} is deleted.".format(product_id), 200

api.add_resource(CompanyProductList, "/company/<int:company_id>/products")
api.add_resource(CompanyList, "/companies")
api.add_resource(CompanyProduct,
                 "/company/<int:company_id>/product/<int:product_id>")

sales = [
    {
        "sale_id": 1,
        "company_id": 1,
        "product_id": 1,
        "name": "laptop",
        "quantity": 42,
        "status": "true",
        "unit_price": 2000000
    }
]


class SaleCreate(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("name")
        parser.add_argument("company_id")
        parser.add_argument("product_id")
        parser.add_argument("quantity")
        parser.add_argument("status")
        parser.add_argument("unit_price")
        args = parser.parse_args()
        flat = False

        for product in products:
            if (str(product['product_id']) == args['product_id'] and
                    str(product['company_id']) == args['company_id']):
                flat = True
                num = int(product["quantity"]) - int(args["quantity"])
                print(num)
                if (num >= 0):
                    product["quantity"] = num
                else:
                    return 'quantity is less.'
        if flat is False:
            return 'product_id not exists'

        sale = {
            "sale_id": int(sales[-1]['sale_id']) + 1,
            "company_id": args["company_id"],
            "name": args["name"],
            "quantity": args["quantity"],
            "status": args["status"],
            "unit_price": args["unit_price"]
        }

        sales.append(sale)
        return sale, 201


class Sale(Resource):
    def get(self, sale_id):
        for sale in sales:
            if(sale_id == sale["sale_id"]):
                return sale, 200
        return "sale not found", 404

    def put(self, sale_id):
        parser = reqparse.RequestParser()
        parser.add_argument("name")
        parser.add_argument("company_id")
        parser.add_argument("quantity")
        parser.add_argument("status")
        parser.add_argument("unit_price")
        args = parser.parse_args()

        for sale in sales:
            if(sale_id == sale["sale_id"]):
                sale["name"] = args["name"]
                sale["company_id"] = args["company_id"]
                sale["quantity"] = args["quantity"]
                sale["status"] = args["status"]
                sale["unit_price"] = args["unit_price"]
                return sale, 200

        return 'Sale not found', 400

    def delete(self, sale_id):
        global sales
        sales = [sale for sale in sales if sale["sale_id"] != sale_id]
        return "{} is deleted.".format(sale_id), 200


class SaleList(Resource):
    def get(self):
        return sales

api.add_resource(SaleCreate, "/sale")
api.add_resource(Sale, "/sale/<int:sale_id>")
api.add_resource(SaleList, '/sales')

app.run(host="0.0.0.0", port="5002")
