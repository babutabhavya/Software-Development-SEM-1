
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
	$(MAKE) check-format check-import-order lint test

test:
	pipenv run pytest --cov=src --cov-report=html --disable-warnings

help:
	@echo "Available targets:"
	@echo "  run               		: Run the Flask API."
	@echo "  setup          		: Install project dependencies, including development dependencies."
	@echo "  check-format   		: Check code formatting using Black."
	@echo "  format         		: Format code using Black."
	@echo "  check-import-order		: Check import order using isort with a profile for Black."
	@echo "  import-order   		: Organize import order using isort with a profile for Black."
	@echo "  lint           		: Run pylint to lint the code in the ./src directory."
	@echo "  test           		: Run pytest to run all the tests in the ./src directory."
	@echo "  check          		: Check code formatting, import order, and linting."
	@echo "                   		 (Equivalent to running check-format, check-import-order, lint)"
	@echo "  help           		: Display this help message."