from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from cv.api.home import router as home_router
from cv.api.author import router as author_router
from cv.api.experience import router as experience_router


def create_application() -> FastAPI:
    """Application factory."""
    app = FastAPI()
    app.mount('/static', StaticFiles(directory='src/static'), name='static')

    app.include_router(
        router=home_router,
    )
    app.include_router(
        router=author_router,
    )
    app.include_router(
        router=experience_router,
    )
    return app


app = create_application()

