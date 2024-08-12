# CV

Generate resume in PDF format.

## Generate the CV

```shell
uv venv --python 3.12.4 --preview
. .venv/bin/activate.fish           # Activate the virtual environment
uv sync
python src/cv/main.py               # Generate the CV
docker compose up --build -d
docker compose down
```

## Backlog

- render model [nicegui](https://nicegui.io/)
  - do not expose db port
  - check lock file not changed in docker
  - reuse UV_CACHE_DIR
- ci/cd with [github actions](https://docs.github.com/en/actions)
- auth
- editor
- [dev container](https://code.visualstudio.com/docs/devcontainers/containers)

## Links

- [best-resume-font-size-and-type-2063125](https://www.thebalancecareers.com/best-resume-font-size-and-type-2063125)
- [uv](https://docs.astral.sh/uv/)
- [ruff](https://docs.astral.sh/ruff/)
- [playwright](https://playwright.dev/python/)
- [prisma](https://github.com/RobertCraigie/prisma-client-py)
