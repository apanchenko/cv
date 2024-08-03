# CV

Generate resume in PDF format.

## Initial setup

```shell
pyenv local 3.11.4
pip install uv
uv venv
. .venv/bin/activate.fish        # Activate the virtual environment
uv pip install pytest-playwright # Initial install
uv pip freeze | uv pip compile - -o requirements.txt # Lock the current environment.
playwright install               # Install the required browsers
```

## Generate the CV

```shell
uv venv
. .venv/bin/activate.fish        # Activate the virtual environment
uv pip sync requirements.txt     # Install from a requirements.txt file.
python main.py                   # Generate the CV
```

## Links

- [best-resume-font-size-and-type-2063125](https://www.thebalancecareers.com/best-resume-font-size-and-type-2063125)
- [uv](https://pypi.org/project/uv/)
- [playwright](https://playwright.dev/python/)
