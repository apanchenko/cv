from fastapi import APIRouter, Depends, Request, Response
from fastapi.responses import HTMLResponse
from playwright.async_api import Page
from secrets import token_urlsafe

from cv.deps import get_db, get_page
from cv.api.jinja import templates
from prisma import Prisma


router = APIRouter()

@router.get('/')
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


@router.post('/generate')
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
