# CV

Generate resume in PDF format.

## Generate the CV

```shell
docker compose run --rm seed                # seed the database
docker compose down db                      # stop the database

docker compose up --build -d
docker compose down

# dev:
uv venv --python 3.12.4 --preview           # create environment
. .venv/bin/activate.fish                   # activate the environment
uv sync                                     # install dependencies
docker compose run -p 5441:5432 -d db       # run database
prisma db push                              # push schema to database
uvicorn cv.main:app --reload --port 8000    # run local server
```

## Backlog

- editor
- ci/cd with [github actions](https://docs.github.com/en/actions)
- auth
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
