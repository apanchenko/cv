from math import exp
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
    author = await db.author.find_unique(
        where = {'id': author_id},
    )
    return templates.TemplateResponse(
        request=request,
        name='author_edit.html',
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
        name='author.html',
        context={
            'author_id': author.id,
            'author_name': author.name,
        },
    )


@app.get(
    '/exp/{exp_id}',
    response_class=HTMLResponse,
)
async def edit_exp(
    request: Request,
    exp_id: int,
    db: Prisma = Depends(get_db),
) -> HTMLResponse:
    """Get edit experience form."""
    exp = await db.experience.find_unique(
        where = {'id': exp_id},
    )
    return templates.TemplateResponse(
        request=request,
        name='experience_edit.html',
        context={'exp': exp.model_dump()},
    )


@app.put(
    '/exp/{exp_id}',
    response_class=HTMLResponse,
)
async def edit_name(
    request: Request,
    exp_id: int,
    position: Annotated[str, Form()],
    href: Annotated[str, Form()],
    link: Annotated[str, Form()],
    text: Annotated[str, Form()],
    tech: Annotated[str, Form()],
    db: Prisma = Depends(get_db),
) -> HTMLResponse:
    """Put experience."""
    exp = await db.experience.update(
        where = {'id': exp_id},
        data = {
            'position': position,
            'href': href,
            'link': link,
            'text': text,
            'tech': tech,
        },
    )
    return templates.TemplateResponse(
        request=request,
        name='experience.html',
        context={'exp': exp.model_dump()},
    )
