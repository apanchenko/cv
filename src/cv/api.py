from fastapi import Depends, Request, Response
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from playwright.async_api import Page
from secrets import token_urlsafe

from cv.app import create_application
from cv.deps import get_db, get_page
from prisma import Prisma

app = create_application()

templates = Jinja2Templates(directory='src/templates')

@app.get('/')
async def home_page(
    request: Request,
    db: Prisma = Depends(get_db), *,
    header: bool = True,
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
        'include_header': header,
        **author.model_dump(),
    })


@app.post('/generate')
async def generate(
    _request: Request,
    page: Page = Depends(get_page),
) -> Response:
    """Generate PDF."""
    await page.goto(
        url='http://localhost:8000?header=False',
    )

    name = token_urlsafe(16)

    await page.pdf(
        format='A4',
        path=f'src/static/{name}/anton.pdf',
    )
    return Response(
        headers={'HX-Redirect': f'/static/{name}/anton.pdf'},
    )
