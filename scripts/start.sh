#!/bin/bash

port=$1

export ENVIRONMENT="production"

uvicorn app.main:app --port ${port}
