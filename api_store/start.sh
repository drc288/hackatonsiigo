#!/bin/bash
# This scrit run api store
START_PRODUCTS=$(gunicorn api.v1.views.index:app &> /dev/null &)
