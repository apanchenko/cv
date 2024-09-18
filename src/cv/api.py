from typing import Annotated
from fastapi import Depends, Request, Response, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from playwright.async_api import Page
from secrets import token_urlsafe
import jinja_partials

from cv.app import create_application
from cv.deps import get_db, get_page
from prisma import Prisma

app = create_application()

templates = Jinja2Templates(directory='src/templates')
jinja_partials.register_starlette_extensions(templates)

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
        'author': author.model_dump(),
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


@app.get(
    '/edit/name/{author_id}',
    response_class=HTMLResponse,
)
async def edit_name(
    request: Request,
    author_id: int,
    db: Prisma = Depends(get_db),
) -> HTMLResponse:
    """Get edit name form."""
    author = await db.author.find_first()
    return templates.TemplateResponse(
        request=request,
        name='author_name_edit.html',
        context={
            'author_id': author.id,
            'author_name': author.name,
        },
    )


@app.put(
    '/edit/name/{author_id}',
    response_class=HTMLResponse,
)
async def edit_name(
    request: Request,
    author_id: int,
    author_name: Annotated[str, Form()],
    db: Prisma = Depends(get_db),
) -> HTMLResponse:
    """Get edit name form."""
    author = await db.author.update(
        where = {
            'id': author_id
        },
        data = {
            'name': author_name,
        },
    )
    return templates.TemplateResponse(
        request=request,
        name='author_name.html',
        context={
            'author_id': author.id,
            'author_name': author.name,
        },
    )
