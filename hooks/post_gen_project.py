import subprocess
import sys
from pathlib import Path

PROJECT_ROOT_PATH = Path('.').resolve()
DOCKERFILE_PATH = PROJECT_ROOT_PATH / 'Dockerfile'
DOCKERIGNORE_PATH = PROJECT_ROOT_PATH / '.dockerignore'
LICENSES_FOLDER = PROJECT_ROOT_PATH / 'licenses' 
READMES_FOLDER = PROJECT_ROOT_PATH / 'readmes' 
PROJECT_LICENSE_PATH = PROJECT_ROOT_PATH / 'LICENSE'
PROJECT_README_PATH = PROJECT_ROOT_PATH / 'README.md'
TARGET_LICENSE_PATH = LICENSES_FOLDER / '{{cookiecutter.project_license}}.txt'
TARGET_README_PATH = READMES_FOLDER / ('no_docker.md' if '{{cookiecutter.dockerize}}' == 'no' else 'docker.md')
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

# drop specified dependencies
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

# handle Docker


def main():
    """initial repo setup"""
    subprocess.run('git init --initial-branch=main', shell=True)
    
    # LICENSE
    subprocess.run(f'mv {TARGET_LICENSE_PATH} {PROJECT_LICENSE_PATH}', shell=True)
    subprocess.run(f'rm -r {LICENSES_FOLDER}', shell=True)
    
    # pyproject.toml
    if dependencies_to_remove:
        subprocess.run(f'poetry remove {dependencies_to_remove_args}', shell=True)
    
    # README.md
    subprocess.run(f'mv {TARGET_README_PATH} {PROJECT_README_PATH}', shell=True)
    subprocess.run(f'rm -r {READMES_FOLDER}', shell=True)
    
    subprocess.run('poetry install --without dev', shell=True)
    
    # Docker
    if '{{cookiecutter.dockerize}}' == 'no':
        subprocess.run(f'rm {DOCKERFILE_PATH}', shell=True)
        subprocess.run(f'rm {DOCKERIGNORE_PATH}', shell=True)
        raise NotImplementedError('rm poetry-export hook @ https://github.com/atloo1/python-cookiecutter/issues/5')
        
    else:
        subprocess.run('poetry export -f requirements.txt --output requirements.txt', shell=True)
        
    subprocess.run('git add .', shell=True)
    subprocess.run('git commit -m "cookiecutter initial commit"', shell=True)


if __name__ == '__main__':
    main()
    sys.exit(0)
