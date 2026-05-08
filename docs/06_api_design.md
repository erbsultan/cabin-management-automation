# 06 — API Design

## Auth

```text
POST /api/auth/login
POST /api/auth/logout
GET  /api/auth/me
```

## Cabins

```text
GET    /api/cabins
POST   /api/cabins
GET    /api/cabins/{id}
PATCH  /api/cabins/{id}
```

## Rentals

```text
POST /api/rentals/start
POST /api/rentals/{id}/return
POST /api/rentals/{id}/return-manual-on-time
GET  /api/rentals/active
GET  /api/rentals/history
GET  /api/rentals/{id}
```

## Violations

```text
POST /api/violations
GET  /api/violations
GET  /api/students/{login}/violations
```

## Trust Score

```text
GET /api/students/{login}/trust-score
GET /api/students/{login}/trust-events
```

## Dashboard

```text
GET /api/dashboard/live
GET /api/dashboard/stats
```

## Health

```text
GET /health
```

Expected response:

```json
{
  "status": "ok",
  "database": "ok"
}
```

## Backend Responsibility

Backend must:

- validate all input;
- calculate time status using server time;
- check roles and permissions;
- create audit logs;
- create trust events;
- prevent direct trust score edits.
