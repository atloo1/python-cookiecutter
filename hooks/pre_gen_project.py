import re

KEBAB_CASE_REGEX = r'^[-a-zA-Z][-a-zA-Z0-9]+$'
PROJECT_PYTHON_REGEX = r'^>=(\d{1,}).(\d{1,}),<(\d{1,})$'
SEMVER_REGEX = (
	r'^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-((?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)'
	r'(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\+([0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$'
)

# contextualize errors
KEBAB_CASE_EXPLAINER_URL = 'https://en.wikipedia.org/wiki/Letter_case#Kebab_case'
SEMVER_EXPLAINER_URL = 'https://semver.org/#semantic-versioning-specification-semver'

# enforce kebab case
project_name = '{{cookiecutter.project_name_kebab_case}}'
if not re.match(KEBAB_CASE_REGEX, project_name):
	raise ValueError(f'project_name_kebab_case "{project_name}" is not kebab case: {KEBAB_CASE_EXPLAINER_URL}')

# enforce Python requirement format
project_python_range = '{{cookiecutter.project_python_required}}'
re_match = re.match(PROJECT_PYTHON_REGEX, project_python_range)
if not re_match:
	raise ValueError(f'project_python_required "{project_python_range}" is not of the form "<=major.minor,<major"')

min_python_major_version = int(re_match[1])
min_python_minor_version = re_match[2]
max_python_major_version = int(re_match[3])
if min_python_major_version >= max_python_major_version:
	raise ValueError(f'Python {min_python_major_version}.{min_python_minor_version} ≥ {max_python_major_version}.0')

# enforce semver project version
project_version = '{{cookiecutter.project_version}}'
if not re.match(SEMVER_REGEX, project_version):
	raise ValueError(f'project_version "{project_version}" is not semantic versioned: {SEMVER_EXPLAINER_URL}')
