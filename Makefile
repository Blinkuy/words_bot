sync:
	uv sync

format:
	uv run ruff format

run:
	uv run python -m src.main

makemigration:
	uv run alembic revision --autogenerate -m "$(msg)"

migrate:
	uv run alembic upgrade head

undomigration:
	uv run alembic downgrade -1