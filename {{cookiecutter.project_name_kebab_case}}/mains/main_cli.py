"""
TODO docstring

run with:
```
poetry run python -m {{cookiecutter.__project_name_snake_case}}.main --help
```
"""

from pathlib import Path
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
@click.option('--out-filepath', default=DEFAULT_OUT_FILEPATH)
def _main(in_filepath: str, out_filepath: str):
    """Private click CLI for main()."""
    print(f'in_filepath is type {type(in_filepath)}')
    main(in_filepath, out_filepath)


if __name__ == '__main__':
    _main()
