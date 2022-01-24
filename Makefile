lint:
	@poetry run flake8 gendiff

test:
	poetry run coverage run --source=gendiff -m pytest tests

test-coverage:
	poetry run coverage xml

.PHONY: test
