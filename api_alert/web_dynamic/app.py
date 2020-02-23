#!/usr/bin/python3
"""
Flask App that integrates with Checker static HTML Template
"""
from flask import Flask, render_template, url_for


# flask setup
app = Flask(__name__)
app.url_map.strict_slashes = False
port = 5000
host = '0.0.0.0'



@app.route('/')
def companies():
    return render_template('companies.html')


if __name__ == "__main__":
    """
    MAIN Flask App"""
    app.run(host=host, port=port)
