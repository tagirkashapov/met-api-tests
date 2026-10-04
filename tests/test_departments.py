from httpx import AsyncClient

from schemas import DepartmentsResponse


async def test_get_departments(async_client: AsyncClient):
    response = await async_client.get("v1/departments")

    assert response.status_code == 200

    data = DepartmentsResponse.model_validate(response.json())

    assert len(data.departments) > 0
