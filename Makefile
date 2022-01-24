install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

lint:
	@poetry run flake8 gendiff

test:
	poetry run coverage run --source=gendiff -m pytest tests

test-coverage:
	poetry run coverage xml

.PHONY: test
