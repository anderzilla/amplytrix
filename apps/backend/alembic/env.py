import asyncio
import os
from logging.config import fileConfig

from alembic import context
from sqlalchemy import Connection
from sqlalchemy.ext.asyncio import async_engine_from_config

from amplytrix.catalog.infrastructure.database import CatalogBase

config = context.config
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = CatalogBase.metadata


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


def apply_migrations(connection: Connection) -> None:
    context.configure(connection=connection, target_metadata=target_metadata, compare_type=True)
    with context.begin_transaction():
        context.run_migrations()


async def run_explicit_migration_job() -> None:
    database_url = os.getenv("AMPLYTRIX_MIGRATION_DATABASE_URL")
    if database_url:
        config.set_main_option("sqlalchemy.url", database_url)
    engine = async_engine_from_config(
        config.get_section(config.config_ini_section, {}), prefix="sqlalchemy."
    )
    async with engine.connect() as connection:
        await connection.run_sync(apply_migrations)
    await engine.dispose()


def run_migrations_online() -> None:
    arguments = context.get_x_argument(as_dictionary=True)
    if arguments.get("allow_online") != "true":
        raise RuntimeError(
            "Online migrations require an explicit migration job using -x allow_online=true; "
            "service startup must never run them."
        )
    asyncio.run(run_explicit_migration_job())


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
