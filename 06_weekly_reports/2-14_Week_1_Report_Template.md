# 2-14 Weekly Report - Week 1

## Student Information

Student name: Georgy Kuchvalskiy
Group: PX-24
Project ID: 2-14
Project name: Local Chat System
Week number: 1

## Planned Work For This Week

Project setup, repository creation, requirements review, wireframes, database draft, Docker baseline.

## Completed Work

- Set up the main project folder structure from 01 to 08 according to requirements.
- Implemented a basic database draft with users, rooms, and messages tables in 2-14_schema.sql.
- Created a text and layout wireframe inside index.html to plan the chat interface.
- Installed Docker Desktop and started Nginx and PostgreSQL services via docker compose.
- Verified that the local server is running on port 8080 and renders the wireframe correctly.

## GitHub Commits

- commit 1: initial project structure setup
- commit 2: docker configuration and starter html check
- commit 3: added database draft and frontend wireframe layout

## Screenshots / Evidence

- main_page_running.png (Shows localhost:8080 working with the wireframe layout)
- docker_ps_output.png (Shows running app and database containers in Docker Desktop)

## Problems Found

- The docker command failed initially because Docker Desktop was missing on the machine.
- Received a "no configuration file provided" error because the command ran in the root directory while the compose file was inside the 04_docker folder.

## Solutions Applied

- Downloaded and installed Docker Desktop application.
- Fixed the path execution by using the explicit file flag: docker compose -f 04_docker/2-14_docker-compose.yml up -d --build.

## Next Week Plan

- Finalize the full database schema and add relations, keys, and indexes.
- Write initial seed data for test users and roles in 2-14_seed_data.sql.
- Begin working on the active frontend HTML and CSS styles for the chat page.

## Supervisor Notes

To be completed by the practice supervisor if needed.