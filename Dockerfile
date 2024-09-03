FROM python:3.12.4-slim AS build

WORKDIR /opt/

COPY --from=ghcr.io/astral-sh/uv:0.2.34 /uv /bin/uv
COPY pyproject.toml .
COPY uv.lock .

ENV UV_CACHE_DIR=/opt/uv-cache/
RUN --mount=type=cache,target=/opt/uv-cache uv venv &&\
    . .venv/bin/activate &&\
    uv sync --no-dev


FROM python:3.12.4-slim

WORKDIR /opt/
ENV PATH="/opt/.venv/bin:$PATH"

COPY --from=build /opt/.venv /opt/.venv
COPY prisma ./prisma
COPY src ./src

CMD python -m prisma generate &&\
    uvicorn cv.main:app --host 0.0.0.0 --port 8000
