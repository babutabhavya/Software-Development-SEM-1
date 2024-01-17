
run:
	pipenv run python app.py

setup:
	pipenv run pipenv install --dev

help:
	@echo "Available targets:"
	@echo "  run            : Run the Flask API"
	@echo "  install        : Install project dependencies"
	@echo "  help           : Display this help message"