sync:
	uv sync

format:
	uv run ruff format

start_bot:
	uv run python -m src.main

makemigrations:
	uv run alembic revision --autogenerate -m "$(msg)"

migrate:
	uv run alembic upgrade head

undomigration:
	uv run alembic downgrade -1

run:
	$(MAKE) migrate
	$(MAKE) start_bot