from httpx import AsyncClient

from schemas import ObjectsResponse


async def test_get_objects(async_client: AsyncClient):
    response = await async_client.get("v1/objects")

    assert response.status_code == 200

    data = ObjectsResponse.model_validate(response.json())

    assert data.total > 0
    assert len(data.objectIDs) > 0
