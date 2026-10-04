import pytest
from httpx import AsyncClient

from logger import log_request, log_response


@pytest.fixture
async def async_client():
    async with AsyncClient(
        base_url="https://collectionapi.metmuseum.org/public/collection",
        headers={
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/120.0.0.0 Safari/537.36"
            )
        },
        timeout=30,
        event_hooks={"request": [log_request], "response": [log_response]}
    ) as ac:
        yield ac
