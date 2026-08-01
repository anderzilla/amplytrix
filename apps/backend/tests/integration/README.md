# PostgreSQL integration tests

Integration tests will use disposable PostgreSQL through Testcontainers or the CI service container when the first SQLAlchemy repository exists. SQLite substitution is prohibited for PostgreSQL behavior. There is no persistence adapter to integrate-test in Phase Zero.
