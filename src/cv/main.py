from fastapi import Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from cv.app import create_application
from cv.deps import get_db
from prisma import Prisma

app = create_application()

templates = Jinja2Templates(directory='src/templates')

@app.get('/')
async def home_page(
    request: Request,
    db: Prisma = Depends(get_db),
) -> HTMLResponse:
    """Home page."""
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
