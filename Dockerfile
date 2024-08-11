FROM python:3.12.4-slim-bullseye
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

WORKDIR /opt/project/
ENV PYTHONPATH=/opt/project/src

COPY cv.html .
COPY icofont.css .
COPY icofont.min.css .
COPY pyproject.toml .
COPY README.md .
COPY uv.lock .
COPY fonts ./fonts
COPY prisma ./prisma
COPY src ./src

RUN uv pip install --system -n -r pyproject.toml

CMD ["python", "src/cv/main.py"]
