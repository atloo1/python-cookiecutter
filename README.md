# python-cookiecutter

[![Dynamic TOML Badge](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2Fatloo1%2Fpython-cookiecutter%2Frefs%2Fheads%2Fmain%2Fpyproject.toml&query=%24.project.requires-python&label=python)](https://github.com/atloo1/python-cookiecutter/blob/main/pyproject.toml)
[![Dynamic TOML Badge](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2Fatloo1%2Fpython-cookiecutter%2Frefs%2Fheads%2Fmain%2Fpyproject.toml&query=%24.project.version&label=version)](https://github.com/atloo1/python-cookiecutter/blob/main/pyproject.toml)
[![GitHub License](https://img.shields.io/github/license/atloo1/python-cookiecutter)](https://github.com/atloo1/python-cookiecutter/blob/main/LICENSE)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/atloo1/python-cookiecutter)

[![Poetry](https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json)](https://python-poetry.org/)
[![Renovate enabled](https://img.shields.io/badge/renovate-enabled-brightgreen.svg)](https://renovatebot.com/)

`Poetry` managed Python project template with `pre-commit`, as well as options for opinionated formatting, testing, containerization, & CI/CD.

## prerequisites

- ### [`cruft`](https://github.com/cruft/cruft?tab=readme-ov-file#installation) (recommended), [`cookiecutter`](https://github.com/cookiecutter/cookiecutter?tab=readme-ov-file#installation), or [`Poetry`](https://python-poetry.org/docs/#installing-with-pipx)

## run

- ### remotely

  - #### with `cruft` (recommended)

    ```
    cruft create https://github.com/atloo1/python-cookiecutter
    ```

  - #### with `cookiecutter`

    ```
    cookiecutter https://github.com/atloo1/python-cookiecutter
    ```

- ### locally

  - #### step 1

    ```
    git clone https://github.com/atloo1/python-cookiecutter.git
    ```

  - #### step 2: with `cruft` via `Poetry`

    ```
    cd python-cookiecutter/
    poetry install
    poetry run cruft .
    mv <resulting-repo>/ ../
    ```

  - #### step 2: with `cookiecutter`

    ```
    cookiecutter python-cookiecutter/
    ```

## template options

`project_name_kebab_case`: project name slug AKA [kebab case](https://en.wikipedia.org/wiki/Letter_case#Kebab_case)

`project_author_name`: author's name*

`project_author_email`: (optional) author's email*

`project_description`: brief project description for `pyproject.toml` & `README.md` headline.

`project_license`: multiple choices of common open source licenses & a DIY proprietary one

`project_python_required`: project's Python version range

`project_version`: [semver](https://semver.org/#semantic-versioning-specification-semver) project version

`dockerize`: containerize the project?

`include_cli`: use a [`click`](https://click.palletsprojects.com/en/stable/) command line interface?

`include_renovate`: use [Renovate](https://docs.renovatebot.com/#renovate-documentation) dependency updater?

`include_testing`: use [pytest](https://docs.pytest.org/en/stable/) & a corresponding [GitHub action](https://github.com/atloo1/python-cookiecutter/blob/main/%7B%7Bcookiecutter.project_name_kebab_case%7D%7D/.github/workflows/ci.yaml) step?

`opinionated_formatting`: enforce syntax compliance according to [`.pre-commit-config.yaml`](https://github.com/atloo1/python-cookiecutter/blob/main/%7B%7Bcookiecutter.project_name_kebab_case%7D%7D/.pre-commit-config.yaml), principally, [`mypy`](https://mypy-lang.org/) & [`ruff`](https://docs.astral.sh/ruff/)?

\* only single author supported: append more to `pyproject.toml` post generation
