#!/bin/bash
# This scipt execute all the services
# run api alert
gunicorn -b 0.0.0.0:5000 api.v1.app:app &> /dev/null &
