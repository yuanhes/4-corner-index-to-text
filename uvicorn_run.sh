#!/bin/bash

nohup 2>&1 uvicorn app:app --host 0.0.0.0 --port 8000 &

## ps -aux | grep uvicorn
## kill xxxx
## run this script

## /usr/bin/python3 /usr/local/bin/uvicorn app:app --host 0.0.0.0 --port 8000
