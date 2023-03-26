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
	poetry run flake8 brain_games
reinstall:
	python3 -m pip install --user --force-reinstall dist/*.whl