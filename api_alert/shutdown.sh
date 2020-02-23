#!/bin/bash
# This script remove the process gunicorn and shut down the service

PROCESS=$(ps aux | grep gunicorn | awk '{print $2; exit}')
kill -9 $PROCESS
