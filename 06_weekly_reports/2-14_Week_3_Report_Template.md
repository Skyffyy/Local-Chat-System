# 2-14 Weekly Report - Week 3

## Student Information

Student name: Georgy Kuchvalskiy
Group: PX-24
Project ID: 2-14
Project name: Local Chat System
Week number: 3

## Planned Work For This Week

Main feature implementation, validation, authentication if required, UI improvements, integration testing.

## Completed Work

- Implemented message search endpoint using PostgreSQL ILIKE for case-insensitive keyword matching.
- Added search bar in the frontend that filters messages in real time as the user types.
- Added keyword highlighting in search results using a custom highlightText function.
- Implemented user status workflow (Active/Banned) with a new PATCH endpoint to update user status.
- Added ban/unban button in the frontend user list with visual status indicator (green/red dot).
- Implemented simple authentication system with a login endpoint that checks username and password using sha256 hashing.
- Updated seed data with properly hashed passwords for all test users.
- Added a login screen in the frontend that blocks access to the chat until the user logs in.
- Login checks user status and rejects banned users with a 403 error.
- Wrote 4 new unit tests for the login endpoint covering success, wrong password, user not found, and banned user cases.
- Wrote 3 new unit tests for the user status update endpoint.
- Wrote 2 new unit tests for the message search endpoint.
- Created a separate integration test file that connects to the real PostgreSQL database instead of using mocks.
- Integration tests verify database connection, seed data integrity, insert/delete operations, and foreign key cascade delete behavior.
- All 23 unit tests and 5 integration tests pass successfully.

## GitHub Commits

- add message search with keyword highlight
- add user status update endpoint with tests
- add ban and unban button for users in frontend
- add login authentication and integration tests with real database

## Screenshots / Evidence

- swagger_ban_user.png - PATCH /api/users/id/status successfully banning a user
- swagger_login.png - POST /api/login successful authentication response
- frontend_login_screen.png - login screen shown before accessing the chat
- frontend_user_before_ban.png - user list showing active user with ban button
- frontend_user_banned.png - user list showing banned user with red status indicator
- frontend_search_highlight.png - message search with highlighted keyword match
- pytest_23_passed.png - all 23 unit tests passing with mocked database
- pytest_integration_5_passed.png - all 5 integration tests passing with real database

## Problems Found

- Seed data originally used fake placeholder password hashes that did not match any real password, so login always failed during testing.
- Docker volume kept old database data even after updating seed_data.sql, so new password hashes were not applied.
- pytest failed to run async integration tests with error "async def functions are not natively supported".

## Solutions Applied

- Generated real sha256 hashes for test passwords (admin123, georgy123, guest123) and updated seed_data.sql with the correct hashes.
- Used docker compose down -v to remove the old database volume and force reseeding with the new password hashes.
- Installed pytest-asyncio and created a pytest.ini file with asyncio_mode = auto so async test functions run correctly.

## Next Week Plan

- Final testing and bug fixing across the whole application.
- Improve error handling and edge cases in the frontend.
- Clean up code comments and remove any leftover debug code.
- Complete final documentation and final internship report.
- Take final screenshots for delivery checklist.
- Clean up GitHub repository structure before final submission.

## Supervisor Notes

To be completed by the practice supervisor if needed.