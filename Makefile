.PHONY: clean lint format test coverage docs help
.DEFAULT_GOAL := help

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

clean: ## remove all build, test, coverage and Python artifacts
	hatch clean

lint: ## check style with ruff
	hatch run lint:ruff check .

format: ## format code with ruff
	hatch run lint:ruff format .

test: ## run tests quickly with the default Python
	hatch run test

coverage: ## check code coverage quickly with the default Python
	hatch run cov

docs: ## generate Sphinx HTML documentation, including API docs
	$(MAKE) -C docs clean
	$(MAKE) -C docs html

servedocs: docs ## compile the docs watching for changes
	watchmedo shell-command -p '*.rst' -c '$(MAKE) -C docs html' -R -D .

release: ## package and upload a release
	hatch build
	hatch publish

build: ## builds source and wheel package
	hatch build

install: clean ## install the package to the active Python's site-packages
	pip install .