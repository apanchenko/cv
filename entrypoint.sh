#!/bin/sh
python -m prisma db push
python -m cv.push_anton
uvicorn cv.main:app --host 0.0.0.0 --port 8000