import pytest
from fastapi import status

@pytest.mark.parametrize("username, expected_status", [
    ("validuser", status.HTTP_201_CREATED),
    ("short", status.HTTP_422_UNPROCESSABLE_ENTITY),  # Too short
    ("thisusernameistoolongforvalidation", status.HTTP_422_UNPROCESSABLE_ENTITY),  # Too long
    ("invalid@user", status.HTTP_422_UNPROCESSABLE_ENTITY),  # Special chars
    ("ADMIN", status.HTTP_422_UNPROCESSABLE_ENTITY),  # Reserved name
    ("123user", status.HTTP_201_CREATED),  # Valid
    ("user_name", status.HTTP_201_CREATED),  # Valid with underscore
])
def test_username_validation(client, username, expected_status):
    response = client.post("/users/", json={
        "username": username,
        "email": f"{username}@example.com",
        "password": "ValidPass123!"
    })
    assert response.status_code == expected_status

def test_update_username_validation(client, test_user, user_token_headers):
    # Test valid update
    response = client.put(
        f"/users/{test_user['id']}",
        headers=user_token_headers,
        json={"username": "new_valid_name"}
    )
    assert response.status_code == status.HTTP_200_OK
    
    # Test invalid update
    response = client.put(
        f"/users/{test_user['id']}",
        headers=user_token_headers,
        json={"username": "invalid@name"}
    )
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
