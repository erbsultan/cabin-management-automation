# 04 — Architecture

## Recommended Application Stack

```text
Frontend: Next.js / React
Backend: FastAPI
Database: PostgreSQL
Realtime MVP: polling every 3–5 seconds
Realtime future upgrade: WebSocket
Reverse proxy: Caddy or Nginx
Deployment: Docker Compose
```

## MVP Architecture

```text
Guard / ADM Browser
        │
        │ HTTPS
        ▼
Reverse Proxy
Caddy / Nginx
        │
        ├── Frontend: Next.js
        │
        ▼
Backend: FastAPI
Business logic, auth, roles, timers
        │
        ▼
Database: PostgreSQL
students, cabins, rentals, violations, trust_events, audit_logs
```

## Realtime Options

### Option 1 — Polling

Frontend asks backend every 3–5 seconds:

```text
GET /api/dashboard/live
```

Pros:

- simple;
- reliable;
- good enough for MVP.

Cons:

- not truly instant;
- small delay.

### Option 2 — WebSocket

Backend sends updates to dashboard instantly.

Pros:

- true live updates;
- better user experience.

Cons:

- more complex;
- better as phase 2 upgrade.

## Recommended Path

Start with polling.

Upgrade to WebSocket later.
