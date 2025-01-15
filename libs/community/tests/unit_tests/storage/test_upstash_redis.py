"""Light weight unit test that attempts to import UpstashRedisStore."""

import pytest


@pytest.mark.requires("upstash_redis")
def test_import_storage() -> None:
    from aibaba_ai_community.storage.upstash_redis import UpstashRedisStore  # noqa
