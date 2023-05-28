install:
	poetry install

gendiff:
	poetry run gendiff

package-install:
	python3 -m pip install --user dist/*.whl
lint:
	poetry run flake8 gendiff
reinstall:
	python3 -m pip install --user --force-reinstall dist/*.whl
test:
	poetry run pytest
test-coverage:
	poetry run pytest --cov=hexlet_code --cov-report xml
selfcheck:
	poetry check

check: selfcheck test lint

build: check
	poetry build

.PHONY: install test lint selfcheck check build