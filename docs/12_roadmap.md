# 12 — Roadmap

## Phase 0 — Documentation Foundation

- Create repository
- Add documentation
- Add folder structure
- Add `.gitignore`
- Add `.env.example`
- Push first commit

## Phase 1 — Backend Skeleton

- Create FastAPI project
- Add PostgreSQL connection
- Add SQLAlchemy
- Add Alembic migrations
- Create `/health`
- Create first models

## Phase 2 — Auth and Roles

- Login
- JWT/session auth
- Roles: guard, adm, admin
- Permission checks on backend

## Phase 3 — Rental Logic

- Issue key
- Return key
- Calculate due_at
- Calculate grace_until
- Calculate ACTIVE/GRACE/OVERDUE
- Manual return override
- Audit log

## Phase 4 — Frontend MVP

- Login page
- Guard dashboard
- Cabin list
- Issue key form
- Active rentals table
- Return key button
- Manual override button
- Add violation form

## Phase 5 — ADM Dashboard

- Live dashboard
- History
- Filters
- Student profile
- Trust score graph
- Violations list

## Phase 6 — Docker Compose

- Backend container
- Frontend container
- PostgreSQL container
- Reverse proxy
- Local full-stack launch

## Phase 7 — Security Hardening

- Input validation
- Backend permission checks
- Audit log everywhere
- Secure secrets
- Rate limiting later
- Security headers
- Basic scanning

## Phase 8 — Monitoring

- Node Exporter
- Prometheus
- Grafana
- Health checks
- Basic alerts

## Phase 9 — Vultr Deployment

- VPS setup
- Firewall
- Docker
- Domain
- HTTPS
- Backups
- Monitoring

## Phase 10 — Future Upgrades

- WebSocket live updates
- Intra/OAuth verification
- QR confirmation
- Telegram notifications
- SMS verification if possible
- Kubernetes
- CI/CD production deploy
- Advanced analytics
