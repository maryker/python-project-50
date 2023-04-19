install:
	poetry install
build:
	poetry build
gendiff:
	poetry run gendiff
publish:
	poetry publish --dry-run
package-install:
	python3 -m pip install --user dist/*.whl
lint:
	poetry run flake8 hexlet_code
reinstall:
	python3 -m pip install --user --force-reinstall dist/*.whl
test:
	poetry run pytest