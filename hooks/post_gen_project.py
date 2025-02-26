import subprocess
import sys
from pathlib import Path

PROJECT_ROOT_PATH = Path('.').resolve()
CI_YAML_PATH = PROJECT_ROOT_PATH / '.github/workflows/ci.yaml'
DOCKERFILE_PATH = PROJECT_ROOT_PATH / 'Dockerfile'
DOCKERIGNORE_PATH = PROJECT_ROOT_PATH / '.dockerignore'
RENOVATE_PATH = PROJECT_ROOT_PATH / '.github/renovate.json'
TESTS_FOLDER = PROJECT_ROOT_PATH / 'tests'
PROJECT_MAIN_PATH = PROJECT_ROOT_PATH / '{cookiecutter.__project_name_snake_case}/main.py'
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
for option, dependencies in [
	('{{cookiecutter.include_cli}}', CLI_DEPENDENCIES),
	('{{cookiecutter.opinionated_formatting}}', FORMATTING_DEPENDENCIES),
	('{{cookiecutter.include_testing}}', TESTING_DEPENDENCIES),
]:
	if option == 'no':
		dependencies_to_remove |= dependencies
DEPENDENCIES_TO_REMOVE = ' '.join(dependencies_to_remove)


def main():
	"""initial repo setup"""
	subprocess.run('git init --initial-branch=main', shell=True)

	# pyproject.toml
	if dependencies_to_remove:
		subprocess.run(f'poetry remove {DEPENDENCIES_TO_REMOVE}', shell=True)

	# testing
	if '{{cookiecutter.include_testing}}' == 'no':
		subprocess.run(f'rm -r {TESTS_FOLDER}', shell=True)

	# renovate
	if '{{cookiecutter.include_renovate}}' == 'no':
		subprocess.run(f'rm {RENOVATE_PATH}', shell=True)

	subprocess.run('poetry install --without dev', shell=True)

	# Docker
	if '{{cookiecutter.dockerize}}' == 'no':
		subprocess.run(f'rm {DOCKERFILE_PATH}', shell=True)
		subprocess.run(f'rm {DOCKERIGNORE_PATH}', shell=True)

	else:
		subprocess.run('poetry export -f requirements.txt --output requirements.txt', shell=True)

	# continuous integration on GitHub runners
	if '{{cookiecutter.continuous_integration}}' == 'no':
		subprocess.run(f'rm {CI_YAML_PATH}', shell=True)

		# initial commit
	subprocess.run('git add .', shell=True)
	subprocess.run('git commit -m v{{cookiecutter.project_version}}', shell=True)

	subprocess.run('poetry install', shell=True)
	subprocess.run('poetry run pre-commit install', shell=True)
	subprocess.run('poetry run pre-commit run --all-files', shell=True)
	subprocess.run('git add .', shell=True)
	subprocess.run('git commit -m "linting"', shell=True)


if __name__ == '__main__':
	main()
	sys.exit(0)
