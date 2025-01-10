# python-cookiecutter

[![Dynamic TOML Badge](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2Fatloo1%2Fpython-cookiecutter%2Frefs%2Fheads%2Fmain%2Fpyproject.toml&query=%24.project.requires-python&label=python)](https://github.com/atloo1/python-cookiecutter/blob/main/pyproject.toml)
[![Dynamic TOML Badge](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2Fatloo1%2Fpython-cookiecutter%2Frefs%2Fheads%2Fmain%2Fpyproject.toml&query=%24.project.version&label=version)](https://github.com/atloo1/python-cookiecutter/blob/main/pyproject.toml)
[![GitHub License](https://img.shields.io/github/license/atloo1/python-cookiecutter)](https://github.com/atloo1/python-cookiecutter/blob/main/LICENSE)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/atloo1/python-cookiecutter)

[![Poetry](https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json)](https://python-poetry.org/)
[![Renovate enabled](https://img.shields.io/badge/renovate-enabled-brightgreen.svg)](https://renovatebot.com/)

`Poetry` managed Python project template with `pre-commit`, as well as options for opinionated formatting, testing, containerization, & CI/CD.

## prerequisites

- ### [cruft](https://github.com/cruft/cruft?tab=readme-ov-file#installation) (recommended) or [cookiecutter](https://github.com/cookiecutter/cookiecutter?tab=readme-ov-file#installation)

## run

- ### remotely with cruft (recommended)

    ```
    cruft create https://github.com/atloo1/python-cookiecutter
    ```

- ### remotely with cookiecutter

  ```
  cookiecutter https://github.com/atloo1/python-cookiecutter.git
  ```
  
- ### locally with cookiecutter

  ```
  git clone https://github.com/atloo1/python-cookiecutter.git
  cookiecutter python-cookiecutter/
  ```
