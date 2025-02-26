# {{cookiecutter.project_name_kebab_case}}

[![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/atloo1/{{cookiecutter.project_name_kebab_case}}/ci.yaml)](https://github.com/atloo1/{{cookiecutter.project_name_kebab_case}}/actions/workflows/ci.yaml?query=branch%3Amain)
[![Dynamic TOML Badge](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2Fatloo1%2F{{cookiecutter.project_name_kebab_case}}%2Frefs%2Fheads%2Fmain%2Fpyproject.toml&query=%24.tool.poetry.dependencies.python&label=python)](https://github.com/atloo1/{{cookiecutter.project_name_kebab_case}}/blob/main/pyproject.toml)
[![Dynamic TOML Badge](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2Fatloo1%2F{{cookiecutter.project_name_kebab_case}}%2Frefs%2Fheads%2Fmain%2Fpyproject.toml&query=%24.tool.poetry.version&label=version)](https://github.com/atloo1/{{cookiecutter.project_name_kebab_case}}/blob/main/pyproject.toml)
[![GitHub License](https://img.shields.io/github/license/atloo1/{{cookiecutter.project_name_kebab_case}})](https://github.com/atloo1/{{cookiecutter.project_name_kebab_case}}/blob/main/LICENSE)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/atloo1/{{cookiecutter.project_name_kebab_case}})

{% if cookiecutter.opinionated_formatting == 'yes' %}[![Checked with mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](https://mypy-lang.org/)
{% endif %}[![Poetry](https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json)](https://python-poetry.org/)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
{% if cookiecutter.include_renovate == 'yes' %}[![Renovate enabled](https://img.shields.io/badge/renovate-enabled-brightgreen.svg)](https://renovatebot.com/)
{% endif %}{% if cookiecutter.opinionated_formatting == 'yes' %}[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
{% endif %}
{{cookiecutter.project_description}}

## prerequisites
{% if cookiecutter.dockerize == 'no' %}
### minimum
{% endif %}
```
git clone {{cookiecutter.__project_url}}.git
cd {{cookiecutter.project_name_kebab_case}}
```
{% if cookiecutter.dockerize == 'no' %}
### recommended: virtual environment setup with [pyenv](https://github.com/pyenv/pyenv?tab=readme-ov-file#installation)

```
pyenv install {{cookiecutter.project_python_required.split('>=')[1].split(',')[0]}} --skip-existing
pyenv local {{cookiecutter.project_python_required.split('>=')[1].split(',')[0]}}
```
{% endif %}
{%- if cookiecutter.dockerize == 'yes' %}
## run

- ### via [Docker](https://docs.docker.com/get-started/get-docker/)
  - #### step 1
    ```
    docker build . -t {{cookiecutter.__project_name_snake_case}}
    ```
  - #### step 2 (for Bash users)
    ```
    docker run \
      --name {{cookiecutter.__project_name_snake_case}} \
      {{cookiecutter.__project_name_snake_case}}
    ```
  - #### step 2 (for PowerShell users)
    ```
    docker run `
      --name {{cookiecutter.__project_name_snake_case}} `
      {{cookiecutter.__project_name_snake_case}}
    ```
  - #### step 3
    ```
    docker rm {{cookiecutter.__project_name_snake_case}}
    ```
- ### via Python interpreter with [Poetry](https://python-poetry.org/docs/#installing-with-pipx)
  - #### step 1 (recommended): virtual environment setup with [pyenv](https://github.com/pyenv/pyenv?tab=readme-ov-file#installation)
    ```
    pyenv install {{cookiecutter.project_python_required.split('>=')[1].split(',')[0]}} --skip-existing
    pyenv local {{cookiecutter.project_python_required.split('>=')[1].split(',')[0]}}
    ```
  - #### step 2
    ```
    poetry install --without dev
    poetry run python -m {{cookiecutter.__project_name_snake_case}}.main{% if cookiecutter.include_cli == 'yes' %} --help{% endif %}
    ```
{% else %}
## run (with [Poetry](https://python-poetry.org/docs/#installing-with-pipx))

```
poetry install --without dev
poetry run python -m {{cookiecutter.__project_name_snake_case}}.main{% if cookiecutter.include_cli == 'yes' %} --help{% endif %}
```
{% endif %}
## develop

- ### [Poetry](https://python-poetry.org/docs/#installing-with-pipx) setup
  ```
  poetry install
  poetry run pre-commit install
  ```
- ### proactively pre-commit
  ```
  poetry run pre-commit run --all-files
  ```
{% if cookiecutter.include_testing == 'yes' -%}
- ### proactively test locally, mirroring the GitHub action
  ```
  poetry run pytest
  ```
{% endif %}
{%- if cookiecutter.include_renovate == 'yes' -%}
- ### [give Renovate repository access](https://github.com/apps/renovate) if setting up own CI/CD
{% endif %}