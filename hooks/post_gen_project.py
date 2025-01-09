import subprocess
import sys
from pathlib import Path

PROJECT_ROOT_PATH = Path('.').resolve()
LICENSES_FOLDER = PROJECT_ROOT_PATH / 'licenses' 
TARGET_LICENSE_FILEPATH = LICENSES_FOLDER / '{{cookiecutter.project_license}}.txt'
PROJECT_LICENSE_FILEPATH = PROJECT_ROOT_PATH / 'LICENSE'


def main():
    """initial repo setup"""
    subprocess.run('git init --initial-branch=main', shell=True)
    subprocess.run([
        'mv',
        TARGET_LICENSE_FILEPATH,
        PROJECT_LICENSE_FILEPATH,
    ])
    subprocess.run(f'rm -r {LICENSES_FOLDER}', shell=True)
    # TODO consider groups remaining; it could just call for poetry install
    subprocess.run('poetry install --without dev', shell=True)
    subprocess.run('git add .', shell=True)
    subprocess.run('git commit -m "cookiecutter initial commit"', shell=True)


if __name__ == '__main__':
    main()
    sys.exit(0)
