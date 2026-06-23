# 2-14 Docker Instructions

## Start

```bash
cd 04_docker
docker compose -f 2-14_docker-compose.yml up -d --build
```

## Check Containers

```bash
docker compose -f 2-14_docker-compose.yml ps
```

## View Logs

```bash
docker compose -f 2-14_docker-compose.yml logs -f
```

## Stop

```bash
docker compose -f 2-14_docker-compose.yml down
```

## Reset Database

```bash
docker compose -f 2-14_docker-compose.yml down -v
docker compose -f 2-14_docker-compose.yml up -d --build
```

## Required Evidence

The student must add screenshots showing:

- Docker containers running.
- Application page opened in browser.
- Database container logs without fatal errors.
