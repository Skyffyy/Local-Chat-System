import pytest
import asyncpg

# Integration tests - these connect to a REAL database, not a mock
# Docker containers must be running before running this file
DATABASE_URL = "postgresql://chat_user:chat_password@localhost:5432/local_chat_db"


@pytest.mark.asyncio
async def test_database_connection():
    # Check that we can actually connect to the real database
    conn = await asyncpg.connect(DATABASE_URL)
    assert conn is not None
    await conn.close()


@pytest.mark.asyncio
async def test_seed_rooms_exist():
    # Check that seed data rooms were loaded correctly
    conn = await asyncpg.connect(DATABASE_URL)
    rows = await conn.fetch("SELECT name FROM rooms")
    room_names = [r["name"] for r in rows]
    assert "general" in room_names
    assert "dev_room" in room_names
    await conn.close()


@pytest.mark.asyncio
async def test_seed_users_exist():
    # Check that seed data users were loaded correctly
    conn = await asyncpg.connect(DATABASE_URL)
    rows = await conn.fetch("SELECT username, role FROM users")
    usernames = [r["username"] for r in rows]
    assert "admin" in usernames
    assert "georgy" in usernames
    await conn.close()


@pytest.mark.asyncio
async def test_insert_and_delete_message():
    # Insert a real message, verify it exists, then clean it up
    conn = await asyncpg.connect(DATABASE_URL)

    row = await conn.fetchrow(
        "INSERT INTO messages (room_id, user_id, message_text) VALUES (1, 1, 'integration test message') RETURNING id"
    )
    message_id = row["id"]

    check = await conn.fetchrow("SELECT message_text FROM messages WHERE id = $1", message_id)
    assert check["message_text"] == "integration test message"

    # Clean up - remove the test message so it does not stay in the database
    await conn.execute("DELETE FROM messages WHERE id = $1", message_id)

    await conn.close()


@pytest.mark.asyncio
async def test_foreign_key_cascade_delete():
    # Deleting a room should cascade delete its messages (ON DELETE CASCADE)
    conn = await asyncpg.connect(DATABASE_URL)

    # Create a temporary room just for this test
    room = await conn.fetchrow(
        "INSERT INTO rooms (name, description) VALUES ('temp_test_room', 'for integration test') RETURNING id"
    )
    room_id = room["id"]

    # Add a message to that room
    await conn.execute(
        "INSERT INTO messages (room_id, user_id, message_text) VALUES ($1, 1, 'temp message')",
        room_id
    )

    # Delete the room
    await conn.execute("DELETE FROM rooms WHERE id = $1", room_id)

    # The message should be gone too because of ON DELETE CASCADE
    messages = await conn.fetch("SELECT * FROM messages WHERE room_id = $1", room_id)
    assert len(messages) == 0

    await conn.close()