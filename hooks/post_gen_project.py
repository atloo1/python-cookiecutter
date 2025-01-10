import subprocess
import sys
from pathlib import Path

PROJECT_ROOT_PATH = Path('.').resolve()
DOCKERFILE_PATH = PROJECT_ROOT_PATH / 'Dockerfile'
DOCKERIGNORE_PATH = PROJECT_ROOT_PATH / '.dockerignore'
LICENSES_FOLDER = PROJECT_ROOT_PATH / 'licenses' 
MAINS_FOLDER = PROJECT_ROOT_PATH / 'mains' 
READMES_FOLDER = PROJECT_ROOT_PATH / 'readmes' 
TESTS_FOLDER = PROJECT_ROOT_PATH / 'tests'
PROJECT_LICENSE_PATH = PROJECT_ROOT_PATH / 'LICENSE'
PROJECT_MAIN_PATH = PROJECT_ROOT_PATH / f'{{cookiecutter.__project_name_snake_case}}/main.py' 
PROJECT_README_PATH = PROJECT_ROOT_PATH / 'README.md'
TARGET_LICENSE_PATH = LICENSES_FOLDER / '{{cookiecutter.project_license}}.txt'
TARGET_MAIN_PATH = MAINS_FOLDER / ('main.py' if '{{cookiecutter.include_cli}}' == 'no' else 'main_cli.py')
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
if '{{cookiecutter.opinionated_formatting}}' == 'no':
    dependencies_to_remove |= FORMATTING_DEPENDENCIES
    raise NotImplementedError('https://github.com/atloo1/python-cookiecutter/issues/7')
if '{{cookiecutter.include_testing}}' == 'no':
    dependencies_to_remove |= TESTING_DEPENDENCIES
DEPENDENCIES_TO_REMOVE = ' '.join(list(dependencies_to_remove))




def main():
    """initial repo setup"""
    subprocess.run('git init --initial-branch=main', shell=True)
    
    # LICENSE
    subprocess.run(f'mv {TARGET_LICENSE_PATH} {PROJECT_LICENSE_PATH}', shell=True)
    subprocess.run(f'rm -r {LICENSES_FOLDER}', shell=True)
    
    # pyproject.toml
    if dependencies_to_remove:
        subprocess.run(f'poetry remove {DEPENDENCIES_TO_REMOVE}', shell=True)
    
    # README.md
    subprocess.run(f'mv {TARGET_README_PATH} {PROJECT_README_PATH}', shell=True)
    subprocess.run(f'rm -r {READMES_FOLDER}', shell=True)
    
    # CLI
    subprocess.run(f'mv {TARGET_MAIN_PATH} {PROJECT_MAIN_PATH}', shell=True)
    subprocess.run(f'rm -r {MAINS_FOLDER}', shell=True)
    if '{{cookiecutter.include_cli}}' == 'no':
        raise NotImplementedError('rm --help in README run: https://github.com/atloo1/python-cookiecutter/issues/16')
    
    # testing
    if '{{cookiecutter.include_testing}}' == 'no':
        subprocess.run(f'rm -r {TESTS_FOLDER}', shell=True)
        raise NotImplementedError('edit README: https://github.com/atloo1/python-cookiecutter/issues/7')
        raise NotImplementedError('edit ci.yaml: https://github.com/atloo1/python-cookiecutter/issues/7')
    
    subprocess.run('poetry install --without dev', shell=True)
    
    # Docker
    if '{{cookiecutter.dockerize}}' == 'no':
        subprocess.run(f'rm {DOCKERFILE_PATH}', shell=True)
        subprocess.run(f'rm {DOCKERIGNORE_PATH}', shell=True)
        raise NotImplementedError('rm poetry-export hook: https://github.com/atloo1/python-cookiecutter/issues/5')
        
    else:
        subprocess.run('poetry export -f requirements.txt --output requirements.txt', shell=True)
        
    subprocess.run('git add .', shell=True)
    subprocess.run('git commit -m "cookiecutter initial commit"', shell=True)


if __name__ == '__main__':
    main()
    sys.exit(0)
