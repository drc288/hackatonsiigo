#!/bin/bash
# This script run web the web dynamic
RUN_WEB=$(gunicorn -b 0.0.0.0:5000 web_dynamic.app:app &> /dev/null &)

$RUN_WEB
