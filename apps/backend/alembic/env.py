from logging.config import fileConfig

from alembic import context
from sqlalchemy import MetaData

config = context.config
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = MetaData()


def run_migrations_offline() -> None:
    context.configure(
        url=config.get_main_option("sqlalchemy.url"),
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        compare_type=True,
    )
    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    raise RuntimeError(
        "Online migrations require an explicit, environment-scoped migration job; "
        "service startup must never run them."
    )


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
