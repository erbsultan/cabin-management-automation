# 07 — Security

## Security Goal

Reduce the risk that someone can:

- break the timer;
- add time to themselves;
- edit trust score;
- delete violations;
- delete history;
- access the database;
- bypass roles;
- abuse API endpoints.

## Main Security Rules

1. Timer is calculated only on backend.
2. Frontend only displays data.
3. PostgreSQL is not exposed to the internet.
4. SSH uses keys only.
5. SSH should be restricted by IP or VPN where possible.
6. HTTPS is required.
7. Roles are checked on backend.
8. Trust score cannot be edited directly.
9. All important actions are written to audit log.
10. Secrets are not stored in Git.
11. SQL is handled through ORM or parameterized queries.
12. Input is validated on backend.
13. Backups are created regularly.
14. Monitoring tracks suspicious activity.

## Ports

Public ports:

```text
80/tcp
443/tcp
```

SSH:

```text
22/tcp only from trusted IP or VPN
```

Database:

```text
5432/tcp must not be public
```

Grafana/Prometheus:

```text
not public
only VPN / allowlist / protected access
```

## Business Logic Security

### Timer

Bad:

```text
Timer is decided by browser
```

Good:

```text
Backend stores started_at, due_at, grace_until, returned_at
Backend calculates current status from server time
```

### Trust Score

Bad:

```text
UPDATE students SET trust_score = 100
```

Good:

```text
trust_score = base_score + sum(trust_events)
```

### Time Extension

Guard should not silently extend rental time.

Recommended rule:

```text
Guard can only issue standard limits.
ADM can extend time only with reason.
Every extension creates audit log.
```

## Audit Log

Audit log should record:

- actor;
- action;
- entity;
- time;
- IP address;
- old value;
- new value;
- comment/reason.

Normal users must not be able to delete audit logs.

## Docker Security

Avoid:

```text
privileged: true
mounting docker.sock
running app as root
storing secrets in image
```

Recommended:

```text
non-root containers
fixed image versions
.env excluded from Git
secrets managed carefully
regular updates
```

## CI/CD Security Later

Planned checks:

```text
backend tests
frontend build
lint
dependency scan
Docker image scan
secret scan
```

Possible tools:

```text
Bandit
pip-audit
Trivy
Gitleaks
```
