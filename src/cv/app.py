from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles


def create_application() -> FastAPI:
    """Application factory."""
    app = FastAPI()
    app.mount('/static', StaticFiles(directory='src/static'), name='static')
    return app
