from typing import Annotated
from fastapi import APIRouter, Depends, Request, Form
from fastapi.responses import HTMLResponse

from cv.deps import get_db
from cv.api.jinja import templates
from prisma import Prisma


router = APIRouter(prefix='/author')


@router.get(
    '/{author_id}',
    response_class=HTMLResponse,
)
async def get_name(
    request: Request,
    author_id: int,
    db: Prisma = Depends(get_db),
) -> HTMLResponse:
    """Get name."""
    author = await db.author.find_unique(
        where = {'id': author_id},
    )
    return templates.TemplateResponse(
        request=request,
        name='author.html',
        context={
            'author_id': author.id,
            'author_name': author.name,
        },
    )


@router.get(
    '/{author_id}/edit',
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


@router.put(
    '/{author_id}',
    response_class=HTMLResponse,
)
async def save_name(
    request: Request,
    author_id: int,
    author_name: Annotated[str, Form()],
    db: Prisma = Depends(get_db),
) -> HTMLResponse:
    """Save author."""
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
