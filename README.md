# CV

Generate resume in PDF format.

## Initial development

```shell
uv init
uv venv --python 3.12.4 --preview
source .venv/bin/activate.fish      # Activate the virtual environment
uv add playwright
uv add ruff --dev
playwright install                  # Install the required browsers

uv add prisma
prisma generate
```

## Generate the CV

```shell
uv venv
. .venv/bin/activate.fish           # Activate the virtual environment
uv sync
python src/cv/main.py               # Generate the CV

docker compose -f compose.yml up --build -d
```

## Backlog

- simple model with [prisma](https://github.com/RobertCraigie/prisma-client-py)
- render model [nicegui](https://nicegui.io/)
- ci/cd with [github actions](https://docs.github.com/en/actions)
- auth
- editor
- [dev container](https://code.visualstudio.com/docs/devcontainers/containers)

## Links

- [best-resume-font-size-and-type-2063125](https://www.thebalancecareers.com/best-resume-font-size-and-type-2063125)
- [uv](https://docs.astral.sh/uv/)
- [ruff](https://docs.astral.sh/ruff/)
- [playwright](https://playwright.dev/python/)
