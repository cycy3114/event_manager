import pytest
from fastapi.testclient import TestClient
from app.main import app

@pytest.fixture
def client():
    return TestClient(app)

async def db_session():
    async with get_test_db() as session:
        yield session
