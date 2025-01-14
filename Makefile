lint:
	ruff check .

.PHONY: test

test:
	pytest --cov=gendiff --cov-report=xml tests/
