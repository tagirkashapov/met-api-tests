import pytest
from httpx import AsyncClient

from schemas import ObjectResponse


@pytest.mark.parametrize("object_id", [45734, 436535, 11417, 437394, 247182])
async def test_get_object(async_client: AsyncClient, object_id):
    response = await async_client.get(f"v1/objects/{object_id}")

    assert response.status_code == 200
    
    data = ObjectResponse.model_validate(response.json())

    assert data.objectID == object_id


async def test_get_object_not_found(async_client: AsyncClient):
    response = await async_client.get("v1/objects/999999")
    
    assert response.status_code == 404
