# 2-14 Database Design

## Required Database Objects

The student must prepare a relational database schema for this project.

## Minimum Common Tables

```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(120) NOT NULL,
    email VARCHAR(160) NOT NULL UNIQUE,
    role VARCHAR(50) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE audit_logs (
    id SERIAL PRIMARY KEY,
    user_id INTEGER,
    action VARCHAR(120) NOT NULL,
    entity_name VARCHAR(120) NOT NULL,
    entity_id INTEGER,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
```

## Project-specific Tables

The student must add project-specific tables for: Local Chat System.

Examples of required modelling decisions:

- Identify the main entity of the application.
- Identify supporting entities.
- Add foreign keys.
- Add indexes for searchable fields.
- Add status fields where workflow is required.
- Add timestamps to important tables.

## Required Deliverables

- Entity relationship description.
- SQL schema file.
- Seed data file.
- Short explanation of each table.
- Screenshot proving that the database runs in Docker.
