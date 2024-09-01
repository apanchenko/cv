from fastapi import Depends, FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from prisma import Prisma

from cv.deps import get_db

app = FastAPI()
templates = Jinja2Templates(directory="src/templates")

app.mount("/static", StaticFiles(directory="src/static"), name="static")

@app.get("/")
async def home_page(
    request: Request,
    db: Prisma = Depends(get_db),
):
    author = await db.author.find_first(include={
        'addresses': True,
        'skills': True,
        'educations': True,
        'experiences': True,
    })

    return templates.TemplateResponse('index.html', {
        'request': request,
        **author.model_dump(),
    })
