# Deploy on Docker — Step by Step

Runs the FastAPI app in a container that connects to **Postgres running on your Mac**.

> Key point: inside a container, `localhost` means the container itself — not your Mac / Windows.
> So we pass the DB URL with `host.docker.internal` (your Laptop, seen from inside Docker)
> using `-e DATABASE_URL=...`, which overrides the `localhost` value in `.env`.

---

## Prerequisites

- Docker Desktop is running.
- Postgres is running on your Mac on port `5432` (the `postgres` database already exists).

---

## 1. Go to the project folder

```bash
cd /Users/prateekmishra/Desktop/Vector_1/00_basic_fastapi
```

## 2. Build the image

```bash
docker build -t todo_apis .
```

## 3. Run the container

```bash
docker run -d -p 8000:8000 \
  -e DATABASE_URL="postgresql+asyncpg://prateekmishra:1234@host.docker.internal:5432/postgres" \
  --name todo_api_server todo_apis
```

What each part does:

| Part | Meaning |
|------|---------|
| `-d` | run in background (detached) |
| `-p 8000:8000` | map container port 8000 → your Mac's port 8000 |
| `-e DATABASE_URL=...` | **required** — points the app at your Mac's Postgres (`host.docker.internal`) |
| `--name todo_api_server` | container name |
| `todo_apis` | the image to run |

## 4. Check it started

```bash
docker ps                       # container should be "Up"
docker logs -f todo_api_server  # watch logs; look for "Table Creation is Done.." then Uvicorn running
```

Then open:

- http://localhost:8000/health  → `{"status":"Success"}`
- http://localhost:8000/docs    → interactive API docs

(On first start the app auto-creates the `users` and `todos` tables.)

---

## Rebuild after code changes

```bash
docker stop todo_api_server
docker rm todo_api_server
docker build -t todo_apis .
# then run again (step 3)
```

## Handy commands

```bash
docker logs todo_api_server                 # view logs
docker exec -it todo_api_server sh          # shell inside the container
docker exec todo_api_server env | grep DATABASE_URL   # confirm the URL the app is using
docker stop todo_api_server                 # stop
docker start todo_api_server                # start again
docker rm -f todo_api_server                # force remove
```

---