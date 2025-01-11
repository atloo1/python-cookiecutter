"""
TODO docstring

run with:
```
poetry run python -m {{cookiecutter.__project_name_snake_case}}.main{% if cookiecutter.include_cli == 'yes' %} --help{% endif %}
```
"""

{% if cookiecutter.include_cli == 'yes' %}

from pathlib import Path, PosixPath
from typing import Union

import click

HERE = Path(__file__).resolve()
PROJECT_ROOT = HERE.parent.parent
DEFAULT_IN_FILEPATH = PROJECT_ROOT / 'in.txt'
DEFAULT_OUT_FILEPATH = PROJECT_ROOT / 'out.txt'


def main(
    in_filepath: Union[Path, str] = DEFAULT_IN_FILEPATH,
    out_filepath: Union[Path, str] = DEFAULT_OUT_FILEPATH,
):
    """
    TODO docstring

    :param in_filepath: TODO
    :param out_filepath: TODO
    """
    in_filepath = Path(in_filepath).resolve()
    out_filepath = Path(out_filepath).resolve()

    raise NotImplementedError(f'process {in_filepath}')

    with open(out_filepath, 'w') as f:
        f.write('')


@click.command()
@click.option('--in-filepath', default=DEFAULT_IN_FILEPATH, type=click.Path(exists=True))
@click.option('--out-filepath', default=DEFAULT_OUT_FILEPATH, type=click.Path())
def _main(in_filepath: PosixPath, out_filepath: PosixPath):
    """Private click CLI for main()."""
    main(in_filepath, out_filepath)
    
{% else %}

def main():
    """TODO docstring"""
    raise NotImplementedError

{% endif %}

if __name__ == '__main__':
    {% if cookiecutter.include_cli == 'yes' %}_{% endif %}main()
