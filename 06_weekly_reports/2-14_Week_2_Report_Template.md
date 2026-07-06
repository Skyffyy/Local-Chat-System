# 2-14 Weekly Report - Week 2

## Student Information

Student name: Georgy Kuchvalskiy
Group: PX-24
Project ID: 2-14
Project name: Local Chat System
Week number: 2

## Planned Work For This Week

Core database implementation, backend structure, first API endpoints, frontend skeleton, initial test cases.

## Completed Work

- Rewrote main.py with real asyncpg database connection using environment variables for credentials.
- Implemented full CRUD API endpoints for rooms, messages, and users using FastAPI and PostgreSQL.
- Added input validation with Pydantic models for room and message creation.
- Built frontend chat UI in index.html with JavaScript that loads rooms and users from the API on page start.
- Implemented message sending via POST request and auto-reload after send.
- Added empty state messages and basic error handling in the frontend.
- Wrote 16 pytest test cases covering all endpoints using dependency override pattern to mock the database.
- All 16 tests pass successfully without requiring a real database connection.
- Verified full system works in Docker with all three containers running (database, backend, app).
- Tested all API endpoints manually using Swagger UI at localhost:8000/docs.

## GitHub Commits

- add API endpoints with database connection and test cases
- add frontend chat UI and fix docker backend startup

## Screenshots / Evidence

- docker_ps_week2.png - all three containers running
- docker_backend_startup.png - uvicorn startup complete in backend logs
- swagger_all_endpoints.png - full API documentation in Swagger UI
- swagger_get_rooms.png - GET /api/rooms returning rooms from database
- swagger_post_room.png - POST /api/rooms creating new room with 201 response
- swagger_get_messages.png - GET /api/rooms/1/messages returning messages with usernames
- frontend_rooms_loaded.png - chat UI with rooms loaded in sidebar
- frontend_messages_general.png - messages displayed in general room
- pytest_16_passed.png - all 16 tests passing

## Problems Found

- Backend container was using base python image instead of Dockerfile so pip install ran every time on startup which caused slow container start.
- POST /api/rooms returned 500 error when trying to create a room with duplicate name because unique constraint on rooms table was violated.
- pytest was not found in terminal because VSCode created a new virtual environment without the required packages installed.

## Solutions Applied

- Added DATABASE_URL environment variable to backend service in docker-compose.yml so the connection string is passed correctly.
- Used a unique room name in Swagger test instead of the default placeholder value to avoid duplicate key error.
- Ran pip install -r requirements.txt inside the venv to install all required packages including pytest and httpx.

## Next Week Plan

- Implement user authentication with password hashing.
- Add search and filtering for messages and rooms.
- Improve frontend UI with better styling and mobile support.
- Add admin panel for managing users and rooms.
- Write integration tests with real database connection.

## Supervisor Notes

To be completed by the practice supervisor if needed.