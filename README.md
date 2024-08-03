# CV

Generate resume in PDF format.

## Initial development

```shell
pyenv local 3.11.4
pip install uv
uv init
uv venv
source .venv/bin/activate.fish      # Activate the virtual environment
uv add playwright
uv add ruff --dev
playwright install                  # Install the required browsers
```

## Generate the CV

```shell
uv venv
. .venv/bin/activate.fish           # Activate the virtual environment
uv sync
python src/cv/main.py               # Generate the CV
```

## Links

- [best-resume-font-size-and-type-2063125](https://www.thebalancecareers.com/best-resume-font-size-and-type-2063125)
- [uv](https://docs.astral.sh/uv/)
- [ruff](https://docs.astral.sh/ruff/)
- [playwright](https://playwright.dev/python/)
