# CV

Generate resume in PDF format.

## Generate the CV

```shell
uv venv --python 3.12.4 --preview
. .venv/bin/activate.fish                 # Activate the virtual environment
uv sync
uvicorn cv.main:app --reload --port 5000  # Run local server
docker compose up --build -d
docker compose down

# dev:
prisma db push
prisma migrate dev --name init
prisma migrate deploy
```

## Backlog

- render model
- ci/cd with [github actions](https://docs.github.com/en/actions)
- auth
- editor
- [dev container](https://code.visualstudio.com/docs/devcontainers/containers)
- consider [tailwindcss](https://tailwindcss.com/)

## Links

- [best-resume-font-size-and-type-2063125](https://www.thebalancecareers.com/best-resume-font-size-and-type-2063125)
- [uv](https://docs.astral.sh/uv/)
- [ruff](https://docs.astral.sh/ruff/)
- [playwright](https://playwright.dev/python/)
- [prisma](https://prisma-client-py.readthedocs.io)
- [htmx](https://htmx.org/)
- [examples](https://github.com/marty331/fasthtmx/)
