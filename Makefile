PRJ = todo


.PHONY: test
test:
	pytest tests.py

.PHONY: make cover
cover:
	pytest --cov=$(PRJ) tests.py

.PHONY: requirements-dev
requirements-dev:
	pip install -r requirements-dev.txt

.PHONY: env
env: requirements-dev
	pip install -e .
