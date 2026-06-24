import pytest
from fastapi.testclient import TestClient
from unittest.mock import AsyncMock, patch, MagicMock
from main import app

client = TestClient(app)

# --- Мок для get_db ---

def make_mock_conn(fetch_result=None, fetchrow_result=None, execute_result=None):
    conn = AsyncMock()
    conn.fetch = AsyncMock(return_value=fetch_result or [])
    conn.fetchrow = AsyncMock(return_value=fetchrow_result)
    conn.execute = AsyncMock(return_value=execute_result or "DELETE 1")
    return conn

# =====================
# STATUS
# =====================

def test_status():
    response = client.get("/api/status")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "online"
    assert data["project"] == "2-14"

# =====================
# ROOMS
# =====================

def test_get_rooms_empty():
    async def override():
        conn = make_mock_conn(fetch_result=[])
        yield conn

    app.dependency_overrides[__import__('main').get_db] = override
    response = client.get("/api/rooms")
    assert response.status_code == 200
    assert response.json() == []
    app.dependency_overrides.clear()

def test_get_rooms_returns_list():
    from datetime import datetime
    fake_rooms = [
        {"id": 1, "name": "general", "description": "Main room", "is_private": False, "created_at": datetime.now()},
        {"id": 2, "name": "dev_room", "description": "Dev room", "is_private": False, "created_at": datetime.now()},
    ]

    async def override():
        conn = make_mock_conn(fetch_result=fake_rooms)
        yield conn

    app.dependency_overrides[__import__('main').get_db] = override
    response = client.get("/api/rooms")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 2
    assert data[0]["name"] == "general"
    app.dependency_overrides.clear()

def test_create_room():
    from datetime import datetime
    fake_row = {"id": 3, "name": "test_room", "description": "Test", "is_private": False, "created_at": datetime.now()}

    async def override():
        conn = make_mock_conn(fetchrow_result=fake_row)
        yield conn

    app.dependency_overrides[__import__('main').get_db] = override
    response = client.post("/api/rooms", json={"name": "test_room", "description": "Test", "is_private": False})
    assert response.status_code == 201
    assert response.json()["name"] == "test_room"
    app.dependency_overrides.clear()

def test_create_room_missing_name():
    response = client.post("/api/rooms", json={"description": "No name"})
    assert response.status_code == 422  # Validation error

def test_delete_room_success():
    async def override():
        conn = make_mock_conn(execute_result="DELETE 1")
        yield conn

    app.dependency_overrides[__import__('main').get_db] = override
    response = client.delete("/api/rooms/1")
    assert response.status_code == 204
    app.dependency_overrides.clear()

def test_delete_room_not_found():
    async def override():
        conn = make_mock_conn(execute_result="DELETE 0")
        yield conn

    app.dependency_overrides[__import__('main').get_db] = override
    response = client.delete("/api/rooms/999")
    assert response.status_code == 404
    app.dependency_overrides.clear()

# =====================
# MESSAGES
# =====================

def test_get_messages_empty():
    async def override():
        conn = make_mock_conn(fetch_result=[])
        yield conn

    app.dependency_overrides[__import__('main').get_db] = override
    response = client.get("/api/rooms/1/messages")
    assert response.status_code == 200
    assert response.json() == []
    app.dependency_overrides.clear()

def test_get_messages_with_data():
    from datetime import datetime
    fake_messages = [
        {"id": 1, "message_text": "Hello!", "created_at": datetime.now(), "username": "admin", "role": "Admin"},
        {"id": 2, "message_text": "Hi there", "created_at": datetime.now(), "username": "georgy", "role": "User"},
    ]

    async def override():
        conn = make_mock_conn(fetch_result=fake_messages)
        yield conn

    app.dependency_overrides[__import__('main').get_db] = override
    response = client.get("/api/rooms/1/messages")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert data[0]["username"] == "admin"
    assert "message_text" in data[0]
    app.dependency_overrides.clear()

def test_create_message():
    from datetime import datetime
    fake_row = {"id": 5, "room_id": 1, "user_id": 1, "message_text": "Test msg", "created_at": datetime.now()}

    async def override():
        conn = make_mock_conn(fetchrow_result=fake_row)
        yield conn

    app.dependency_overrides[__import__('main').get_db] = override
    response = client.post("/api/rooms/1/messages", json={"user_id": 1, "message_text": "Test msg"})
    assert response.status_code == 201
    assert response.json()["message_text"] == "Test msg"
    app.dependency_overrides.clear()

def test_create_message_missing_fields():
    response = client.post("/api/rooms/1/messages", json={"message_text": "No user_id"})
    assert response.status_code == 422

def test_delete_message_success():
    async def override():
        conn = make_mock_conn(execute_result="DELETE 1")
        yield conn

    app.dependency_overrides[__import__('main').get_db] = override
    response = client.delete("/api/messages/1")
    assert response.status_code == 204
    app.dependency_overrides.clear()

def test_delete_message_not_found():
    async def override():
        conn = make_mock_conn(execute_result="DELETE 0")
        yield conn

    app.dependency_overrides[__import__('main').get_db] = override
    response = client.delete("/api/messages/999")
    assert response.status_code == 404
    app.dependency_overrides.clear()

# =====================
# USERS
# =====================

def test_get_users():
    from datetime import datetime
    fake_users = [
        {"id": 1, "username": "admin", "role": "Admin", "status": "Active", "created_at": datetime.now()},
        {"id": 2, "username": "georgy", "role": "User", "status": "Active", "created_at": datetime.now()},
    ]

    async def override():
        conn = make_mock_conn(fetch_result=fake_users)
        yield conn

    app.dependency_overrides[__import__('main').get_db] = override
    response = client.get("/api/users")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert data[0]["username"] == "admin"
    assert "password_hash" not in data[0]  # пароль не должен утекать
    app.dependency_overrides.clear()

def test_get_user_by_id():
    from datetime import datetime
    fake_user = {"id": 1, "username": "admin", "role": "Admin", "status": "Active", "created_at": datetime.now()}

    async def override():
        conn = make_mock_conn(fetchrow_result=fake_user)
        yield conn

    app.dependency_overrides[__import__('main').get_db] = override
    response = client.get("/api/users/1")
    assert response.status_code == 200
    assert response.json()["username"] == "admin"
    app.dependency_overrides.clear()

def test_get_user_not_found():
    async def override():
        conn = make_mock_conn(fetchrow_result=None)
        yield conn

    app.dependency_overrides[__import__('main').get_db] = override
    response = client.get("/api/users/999")
    assert response.status_code == 404
    app.dependency_overrides.clear()