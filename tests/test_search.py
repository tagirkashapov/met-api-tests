from httpx import AsyncClient

from schemas import ObjectsResponse, ObjectResponse


async def test_search_by_keyword(async_client: AsyncClient):
    response = await async_client.get("v1.1/search?q=sunflowers")

    assert response.status_code == 200

    data = ObjectsResponse.model_validate(response.json())

    assert data.total > 0
    assert len(data.objectIDs) > 0

    for object_id in data.objectIDs[:5]:
        res = await async_client.get(f"v1/objects/{object_id}")

        assert res.status_code == 200

        obj = ObjectResponse.model_validate(res.json())

        text = " ".join([
            obj.title or "",
            obj.artistDisplayName or "",
            obj.objectName or "",
            obj.medium or "",
            " ".join(tag.term for tag in obj.tags or [])
        ]).lower()

        assert "sunflowers" in text


async def test_search_result_pagination(async_client: AsyncClient):
    response = await async_client.get(
        "v1.1/search?q=sunflowers&offset=5&limit=10"
    )

    assert response.status_code == 200

    data = ObjectsResponse.model_validate(response.json())

    assert data.total >= 15
    assert len(data.objectIDs) == 10


async def test_search_with_filter(async_client: AsyncClient):
    response = await async_client.get(
        "v1.1/search?q=sunflowers&isHighlight=true"
    )

    assert response.status_code == 200

    data = ObjectsResponse.model_validate(response.json())

    for object_id in data.objectIDs[:5]:
        res = await async_client.get(f"v1/objects/{object_id}")

        assert res.status_code == 200

        obj = ObjectResponse.model_validate(res.json())

        assert obj.isHighlight is True
