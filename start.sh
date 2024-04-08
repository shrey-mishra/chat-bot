#!/bin/bash

cd "$(dirname "$0")"
source myenv/scripts/activate
uvicorn app:app --host 0.0.0.0 --workers = 1