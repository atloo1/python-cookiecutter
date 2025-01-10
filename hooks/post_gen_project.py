import subprocess
import sys
from pathlib import Path

PROJECT_ROOT_PATH = Path('.').resolve()
LICENSES_FOLDER = PROJECT_ROOT_PATH / 'licenses' 
TARGET_LICENSE_PATH = LICENSES_FOLDER / '{{cookiecutter.project_license}}.txt'
PROJECT_LICENSE_PATH = PROJECT_ROOT_PATH / 'LICENSE'
CLI_DEPENDENCIES = {
    'click',
}
FORMATTING_DEPENDENCIES = {
    'mypy',
    'ruff',
}
TESTING_DEPENDENCIES = {
    'pytest',
}
dependencies_to_remove = set()
if '{{cookiecutter.include_cli}}' == 'no':
    dependencies_to_remove |= CLI_DEPENDENCIES
    raise NotImplementedError('https://github.com/atloo1/python-cookiecutter/issues/6')
if '{{cookiecutter.enforce_opinionated_formatting}}' == 'no':
    dependencies_to_remove |= FORMATTING_DEPENDENCIES
    raise NotImplementedError('https://github.com/atloo1/python-cookiecutter/issues/7')
if '{{cookiecutter.include_testing}}' == 'no':
    dependencies_to_remove |= TESTING_DEPENDENCIES
    raise NotImplementedError('https://github.com/atloo1/python-cookiecutter/issues/4')
dependencies_to_remove_args = ' '.join(list(dependencies_to_remove))


def main():
    """initial repo setup"""
    subprocess.run('git init --initial-branch=main', shell=True)
    subprocess.run(f'mv {TARGET_LICENSE_PATH} {PROJECT_LICENSE_PATH}', shell=True)
    subprocess.run(f'rm -r {LICENSES_FOLDER}', shell=True)
    if dependencies_to_remove:
        subprocess.run(f'poetry remove {dependencies_to_remove_args}', shell=True)
    if '{{cookiecutter.dockerize}}' == 'no':
        raise NotImplementedError('https://github.com/atloo1/python-cookiecutter/issues/5')
    subprocess.run('poetry install --without dev', shell=True)
    subprocess.run('git add .', shell=True)
    subprocess.run('git commit -m "cookiecutter initial commit"', shell=True)


if __name__ == '__main__':
    main()
    sys.exit(0)
