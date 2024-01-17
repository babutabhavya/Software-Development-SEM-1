
run:
	pipenv run python src/app.py

setup:
	pipenv run pipenv install --dev

check-format:
	pipenv run black ./src --skip-string-normalization --check
	exit $$?

format:
	pipenv run black ./src --skip-string-normalization

check-import-order:
	pipenv run isort **/* --filter-files --profile black -c

import-order:
	isort **/* --filter-files --profile black

lint:
	pipenv run pylint ./src

check:
	$(MAKE) backend-check-format backend-check-import-order backend-lint

help:
	@echo "Available targets:"
	@echo "  run            : Run the Flask API"
	@echo "  install        : Install project dependencies"
	@echo "  help           : Display this help message"