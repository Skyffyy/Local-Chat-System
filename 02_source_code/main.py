from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="2-14 Local Chat System API")

# Allow frontend to connect to backend without CORS security blocks
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Test API endpoint to check server status
@app.get("/api/status")
def get_status():
    return {"status": "online", "project": "2-14", "version": "1.0"}

# Test API endpoint to return sample rooms before DB connection
@app.get("/api/rooms")
def get_rooms():
    return [
        {"id": 1, "name": "general", "description": "Main chat room"},
        {"id": 2, "name": "dev_room", "description": "Room for developers"}
    ]