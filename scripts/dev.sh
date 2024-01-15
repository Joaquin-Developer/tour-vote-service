#!/bin/bash

port=$1

uvicorn app.main:app --port ${port} --reload
