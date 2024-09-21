from typing import Annotated
from fastapi import APIRouter, Depends, Request, Form
from fastapi.responses import HTMLResponse

from cv.deps import get_db
from cv.api.jinja import templates
from prisma import Prisma


router = APIRouter(prefix='/experience')


@router.get(
    '/{exp_id}',
    response_class=HTMLResponse,
)
async def get_experience(
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
        name='experience.html',
        context={'exp': exp.model_dump()},
    )


@router.get(
    '/edit/{exp_id}',
    response_class=HTMLResponse,
)
async def edit_experience(
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


@router.put(
    '/{exp_id}',
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
