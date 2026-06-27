from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import asyncpg
import os

app = FastAPI(title="2-14 Local Chat System API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://chat_user:chat_password@database:5432/local_chat_db"
)

async def get_db():
    conn = await asyncpg.connect(DATABASE_URL)
    try:
        yield conn
    finally:
        await conn.close()

# --- Schemas ---

class MessageCreate(BaseModel):
    user_id: int
    message_text: str

class RoomCreate(BaseModel):
    name: str
    description: Optional[str] = None
    is_private: bool = False

# --- Status ---

@app.get("/api/status")
async def get_status():
    return {"status": "online", "project": "2-14", "version": "2.0"}

# --- Rooms ---

@app.get("/api/rooms")
async def get_rooms(conn=Depends(get_db)):
    rows = await conn.fetch("SELECT id, name, description, is_private, created_at FROM rooms ORDER BY id")
    return [dict(r) for r in rows]

@app.post("/api/rooms", status_code=201)
async def create_room(room: RoomCreate, conn=Depends(get_db)):
    row = await conn.fetchrow(
        "INSERT INTO rooms (name, description, is_private) VALUES ($1, $2, $3) RETURNING *",
        room.name, room.description, room.is_private
    )
    return dict(row)

@app.delete("/api/rooms/{room_id}", status_code=204)
async def delete_room(room_id: int, conn=Depends(get_db)):
    result = await conn.execute("DELETE FROM rooms WHERE id = $1", room_id)
    if result == "DELETE 0":
        raise HTTPException(status_code=404, detail="Room not found")

# --- Messages ---

@app.get("/api/rooms/{room_id}/messages")
async def get_messages(room_id: int, conn=Depends(get_db)):
    rows = await conn.fetch(
        """
        SELECT m.id, m.message_text, m.created_at,
               u.username, u.role
        FROM messages m
        LEFT JOIN users u ON m.user_id = u.id
        WHERE m.room_id = $1
        ORDER BY m.created_at ASC
        """,
        room_id
    )
    return [dict(r) for r in rows]

@app.post("/api/rooms/{room_id}/messages", status_code=201)
async def create_message(room_id: int, msg: MessageCreate, conn=Depends(get_db)):
    row = await conn.fetchrow(
        "INSERT INTO messages (room_id, user_id, message_text) VALUES ($1, $2, $3) RETURNING *",
        room_id, msg.user_id, msg.message_text
    )
    return dict(row)

@app.delete("/api/messages/{message_id}", status_code=204)
async def delete_message(message_id: int, conn=Depends(get_db)):
    result = await conn.execute("DELETE FROM messages WHERE id = $1", message_id)
    if result == "DELETE 0":
        raise HTTPException(status_code=404, detail="Message not found")

# Search messages in a room by keyword
@app.get("/api/rooms/{room_id}/messages/search")
async def search_messages(room_id: int, q: str, conn=Depends(get_db)):
    if not q.strip():
        raise HTTPException(status_code=400, detail="Search query cannot be empty")
    rows = await conn.fetch(
        """
        SELECT m.id, m.message_text, m.created_at,
               u.username, u.role
        FROM messages m
        LEFT JOIN users u ON m.user_id = u.id
        WHERE m.room_id = $1 AND m.message_text ILIKE $2
        ORDER BY m.created_at ASC
        """,
        room_id, f"%{q}%"
    )
    return [dict(r) for r in rows]
# --- Users ---

@app.get("/api/users")
async def get_users(conn=Depends(get_db)):
    rows = await conn.fetch("SELECT id, username, role, status, created_at FROM users ORDER BY id")
    return [dict(r) for r in rows]

@app.get("/api/users/{user_id}")
async def get_user(user_id: int, conn=Depends(get_db)):
    row = await conn.fetchrow(
        "SELECT id, username, role, status, created_at FROM users WHERE id = $1", user_id
    )
    if not row:
        raise HTTPException(status_code=404, detail="User not found")
    return dict(row)