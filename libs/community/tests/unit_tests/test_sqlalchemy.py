import sqlalchemy.orm

import aiagentsforce_community  # noqa: F401


def test_configure_mappers() -> None:
    sqlalchemy.orm.configure_mappers()
