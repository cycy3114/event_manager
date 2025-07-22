import pytest
from fastapi import status
from app.models.user_model import User

@pytest.mark.asyncio
async def test_user_creation(async_client, db_session):
    # Test data
    user_data = {
        "username": "testuser",
        "email": "test@example.com",
        "password": "ValidPass123!"
    }
    
    # Create user
    response = await async_client.post("/users/", json=user_data)
    assert response.status_code == status.HTTP_201_CREATED
    
    # Verify user exists in DB
    result = await db_session.execute("SELECT * FROM users WHERE email = 'test@example.com'")
    user = result.scalars().first()
    assert user is not None
    assert user.email == "test@example.com"
