from fastapi import status
import pytest

@pytest.mark.asyncio
async def test_profile_updates(async_client, test_user, admin_token):
    headers = {"Authorization": f"Bearer {admin_token}"}
    
    # Test empty update
    response = await async_client.put(
        f"/users/{test_user.id}",
        json={},
        headers=headers
    )
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    # Test partial update
    response = await async_client.put(
        f"/users/{test_user.id}",
        json={"bio": "New bio"},
        headers=headers
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["bio"] == "New bio"
