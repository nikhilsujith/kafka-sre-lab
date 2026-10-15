.DEFAULT_GOAL := help
PYTHON ?= python3
VENV   := .venv
BIN    := $(VENV)/bin

.PHONY: help venv install lint format typecheck test check clean up down

help: ## Show available targets
	@grep -E '^[a-zA-Z_-]+:.*?## ' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-12s\033[0m %s\n", $$1, $$2}'

venv: ## Create a virtual environment in .venv
	$(PYTHON) -m venv $(VENV)

install: venv ## Install the package and dev tools, and set up pre-commit hooks
	$(BIN)/pip install --upgrade pip
	$(BIN)/pip install -e ".[dev]"
	$(BIN)/pre-commit install

lint: ## Lint and check formatting
	$(BIN)/ruff check .
	$(BIN)/black --check .

format: ## Auto-format the code
	$(BIN)/ruff check --fix .
	$(BIN)/black .

typecheck: ## Run mypy in strict mode
	$(BIN)/mypy

test: ## Run the test suite with coverage
	$(BIN)/pytest

check: lint typecheck test ## Everything CI runs

clean: ## Remove caches and build output
	rm -rf build dist *.egg-info .pytest_cache .mypy_cache .ruff_cache .coverage htmlcov
	find . -name __pycache__ -type d -prune -exec rm -rf {} +

up: ## Provision infrastructure (available from Week 5)
	@echo "Not wired up yet: see ROADMAP.md, Week 5."

down: ## Destroy all infrastructure (available from Week 5)
	@echo "Not wired up yet: see ROADMAP.md, Week 5."
