# 09 — Monitoring

## What to Monitor

### Server Metrics

- CPU usage
- RAM usage
- disk usage
- network traffic
- Docker container status
- PostgreSQL availability
- backend availability

### Application Metrics

- active rentals
- overdue rentals
- rentals in grace period
- failed login attempts
- 401/403 responses
- 500 errors
- manual overrides
- violations per day
- top late students

### User-Side Monitoring

Server-side monitoring is not enough.

We also need to know how the system responds from the 21 School network.

Example command:

```bash
curl -o /dev/null -s -w "time_total=%{time_total}\n" https://cabins.example.com/health
```

## Planned Tools

```text
Prometheus
Grafana
Node Exporter
Loki later
```

## Health Endpoint

Backend should expose:

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

## Basic Dashboard Panels

Grafana dashboard should include:

- CPU;
- RAM;
- disk;
- uptime;
- backend health;
- database health;
- active rentals;
- overdue rentals;
- failed logins;
- manual overrides;
- violations.
