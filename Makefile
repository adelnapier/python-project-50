lint:
	ruff check .

.PHONY: test

test:
	pytest --cov=gendiff tests/
