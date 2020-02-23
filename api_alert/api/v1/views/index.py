#!/usr/bin/python3
"""
this file has the end point route
"""
from api.v1.views import app_views
from flask import jsonify, request, abort, make_response
import requests
import time

@app_views.route('/status', methods=["GET"])
def json_status():
    """
    return a json file
    """
    
    return jsonify({"status": "OK"})

@app_views.route('/companies', methods=["GET"], strict_slashes=False)
def companies():
    """
    It will list all the companies that we get from a microservice
    """
    res = requests.get('http://0.0.0.0:5002/companies')
  
    return jsonify(res.json())

@app_views.route('/companies/<id>/products', )
    
    
    