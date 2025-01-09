import re

PROJECT_NAME_REGEX = r'^[-a-zA-Z][-a-zA-Z0-9]+$'
PROJECT_VERSION_REGEX = r'^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-((?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\+([0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$'

# contextualize errors
PROJECT_NAME_KEBAB_CASE_ERROR_URL = 'https://en.wikipedia.org/wiki/Letter_case#Kebab_case'
PROJECT_VERSION_ERROR_URL = 'https://semver.org/#semantic-versioning-specification-semver'

project_name = '{{cookiecutter.project_name_kebab_case}}'
if not re.match(PROJECT_NAME_REGEX, project_name):
    raise ValueError(f'project_name_kebab_case "{project_name}" is not kebab case: {PROJECT_NAME_KEBAB_CASE_ERROR_URL}')

project_version = '{{cookiecutter.project_version}}'
if not re.match(PROJECT_VERSION_REGEX, project_version):
    raise ValueError(f'project_version "{project_version}" is not semantic versioned: {PROJECT_VERSION_ERROR_URL}')
