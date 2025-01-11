"""
test ../{{cookiecutter.__project_name_snake_case}}/main.py

run with:
```
poetry run pytest tests/main_test.py
"""

import pytest

from {{cookiecutter.__project_name_snake_case}} import main


def test_main():
    with pytest.raises(NotImplementedError):
        main.main()
