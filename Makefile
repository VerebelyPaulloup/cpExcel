.PHONY: check lint format typecheck complexity test build

check: lint format typecheck complexity test

lint:
	uv run ruff check .

format:
	uv run ruff format --check .

typecheck:
	uv run mypy src/

complexity:
	uv run radon cc . -s 
	uv run xenon --max-absolute B --max-modules B --max-average A .
	uv run radon mi . -s          # maintenability index
	uv run radon raw . 

test:
	uv run pytest

build:
	uv run pyinstaller main.py --onefile --name mon_app

fix:
	uv run ruff check . --fix
	uv run ruff format .

security:
	uv run bandit -r src/
	uv run pip-audit