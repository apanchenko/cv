#!/usr/bin/env python3
import uvicorn
import frontend
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def read_root():
    return {'Hello': 'World'}


frontend.init(app)

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)