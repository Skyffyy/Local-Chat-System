# 2-14 Setup and Run Guide

## 1. Required Tools

Install the following tools:

- Git: https://git-scm.com/doc
- GitHub Docs: https://docs.github.com/
- Docker: https://docs.docker.com/
- Docker Compose: https://docs.docker.com/compose/
- Visual Studio Code: https://code.visualstudio.com/docs
- PostgreSQL Documentation: https://www.postgresql.org/docs/
- MariaDB Documentation: https://mariadb.com/kb/en/documentation/
- MDN HTML: https://developer.mozilla.org/en-US/docs/Web/HTML
- MDN CSS: https://developer.mozilla.org/en-US/docs/Web/CSS
- MDN JavaScript: https://developer.mozilla.org/en-US/docs/Web/JavaScript

## 2. Repository Preparation

Run these commands:

```bash
git init
git branch -M main
git add .
git commit -m "initial project structure"
```

Create a GitHub repository and push the code:

```bash
git remote add origin <your-github-repository-url>
git push -u origin main
```

## 3. Docker Start

From the project root run:

```bash
docker compose up -d --build
docker compose ps
docker compose logs -f
```

## 4. Docker Stop

```bash
docker compose down
```

## 5. Rebuild After Changes

```bash
docker compose down
docker compose up -d --build
```

## 6. Database Initialisation

Place SQL files in the 03_database folder. The schema must create tables, indexes, constraints, and seed test records.

## 7. Common Mistakes to Avoid

- Do not commit passwords.
- Do not hardcode database hostnames.
- Do not keep all code in one file.
- Do not skip validation.
- Do not submit screenshots only without source code.
- Do not forget weekly reports.
