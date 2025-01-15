import sqlalchemy.orm

import aibaba_ai_community  # noqa: F401


def test_configure_mappers() -> None:
    sqlalchemy.orm.configure_mappers()
