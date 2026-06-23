# 2-14 Detailed Requirements - Local Chat System

## 1. Functional Requirements

The student must implement the project described below:

Create a real-time chat application for local teams with rooms, users, and message history.

The application must include clear navigation, structured pages, input forms, validation messages, data listing pages, create/edit/delete flows where relevant, and a simple administration or management area.

## 2. User Roles

Minimum required roles:

- Administrator: can manage all records and system settings.
- Standard user: can view and manage only the records assigned to the normal workflow.
- Guest or public user: can view only public information if the project requires public pages.

## 3. Main Features

The student must analyse the project and implement at least these feature groups:

- Data creation form with validation.
- Data list view with search or filtering.
- Detail page for one selected record.
- Edit functionality.
- Delete or archive functionality.
- Status field or workflow state.
- Basic dashboard or summary page.
- Error handling for incorrect input.
- Empty-state messages when no data exists.
- Basic audit field such as created_at and updated_at.

## 4. Non-functional Requirements

The application must be easy to run locally. The user interface must be readable on laptop and mobile screen sizes. The code must be organised into logical folders. Secrets must not be committed to GitHub. The database must be initialised from scripts. Docker Compose must start the required services.

## 5. Technical Requirements

Use Git for version control. Use GitHub for the final repository. Use Docker Compose for local execution. Use PostgreSQL or MariaDB unless the teacher approves a different database. Use environment variables for database connection settings. Include README instructions that a different student can follow without asking additional questions.

## 6. Documentation Requirements

The student must update all documentation during the project and keep it in GitHub. Documentation must include setup steps, database schema, screenshots, test results, known issues, and final practice report.

## 7. Out of Scope

The student must not use real personal data, real passwords, real payment data, or production systems. The project is a learning project and must be safe to run in a local lab environment.
