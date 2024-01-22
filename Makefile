makemigrations:
	cd lms && pipenv run python manage.py makemigrations

migrate:
	cd lms && pipenv run python manage.py migrate

run:
	cd lms && pipenv run python manage.py runserver

setup:
	cd lms && pipenv run pipenv install --dev

check-format:
	cd lms && pipenv run black ./lms --skip-string-normalization --check --exclude='migrations'
	exit $$?

format:
	cd lms && pipenv run black ./lms --skip-string-normalization --exclude='migrations'

check-import-order:
	cd lms && pipenv run isort **/* --filter-files --profile black -c

import-order:
	cd lms && pipenv run isort **/* --filter-files --profile black

lint:
	cd lms && pipenv run pylint . --load-plugins pylint_django --django-settings-module=lms -v

check:
	$(MAKE) check-format check-import-order lint test

test:
	cd lms && pipenv run pytest --disable-warnings --cov --cov-report=html

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
