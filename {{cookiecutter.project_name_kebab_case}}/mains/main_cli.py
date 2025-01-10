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


def main(in_filepath: Union[Path, str], out_filepath: Union[Path, str]):
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
@click.option('--in-filepath', default='in.txt', type=click.Path(exists=True))
@click.option('--out-filepath', default='out.txt')
def _main(in_filepath: str, out_filepath: str):
    """Private click CLI for main()."""
    main(in_filepath, out_filepath)


if __name__ == '__main__':
    raise NotImplementedError('pass templated pytest')
    _main()
