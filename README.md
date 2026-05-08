# Cabin Management System

Digital key rental and cabin monitoring system for 21 School.

## Problem

Cabin keys are currently managed manually on paper. This makes it hard to track:

- who took a key;
- which cabin is occupied;
- how much time is left;
- who exceeded the limit;
- who returned the key on time;
- who has violations;
- how responsible a student is over time.

## Solution

A web-based system for guards and ADM to manage cabin key rentals, monitor active usage, track grace periods, record violations, and calculate student trust score.

## Main Idea

A student comes to the guard, shows their 21 School/Intra profile, and the guard manually verifies the profile. After that, the guard enters the student's unique login into the system, selects a cabin, sets the time limit, and starts the rental timer.

The system tracks:

- active rentals;
- remaining time;
- grace period;
- overdue rentals;
- returns;
- violations;
- trust score;
- audit logs.

## MVP Features

- Guard/ADM/Admin login
- Role-based access control
- Cabin list
- Key issue and return
- Timer and grace period
- Overdue tracking
- Manual return override
- Comments
- Violations
- Trust events
- Trust score
- Audit logs
- Live dashboard
- Basic monitoring
- Daily PostgreSQL backups

## Stack

Planned stack:

- Frontend: Next.js / React
- Backend: FastAPI
- Database: PostgreSQL
- Deployment: Docker Compose
- Reverse proxy: Caddy or Nginx
- Monitoring: Prometheus + Grafana
- Logs: Loki later

## Documentation

Project documentation is located in [`docs/`](docs/).

Recommended reading order:

1. [`00_project_overview.md`](docs/00_project_overview.md)
2. [`01_requirements.md`](docs/01_requirements.md)
3. [`02_user_roles.md`](docs/02_user_roles.md)
4. [`03_business_flow.md`](docs/03_business_flow.md)
5. [`04_architecture.md`](docs/04_architecture.md)
6. [`05_database_schema.md`](docs/05_database_schema.md)
7. [`06_api_design.md`](docs/06_api_design.md)
8. [`07_security.md`](docs/07_security.md)
9. [`08_infrastructure.md`](docs/08_infrastructure.md)
10. [`09_monitoring.md`](docs/09_monitoring.md)
11. [`10_backup_restore.md`](docs/10_backup_restore.md)
12. [`11_deployment_guide.md`](docs/11_deployment_guide.md)
13. [`12_roadmap.md`](docs/12_roadmap.md)
14. [`13_next_steps.md`](docs/13_next_steps.md)

## Local Development

Coming soon.

## First Milestone

The first milestone is not the full application. The first milestone is the foundation:

- repository created;
- documentation added;
- folder structure created;
- `.gitignore` added;
- `.env.example` added;
- first commit pushed to GitHub.

## Roadmap

1. Documentation and repository foundation
2. Backend skeleton
3. PostgreSQL and migrations
4. Auth and roles
5. Rentals logic
6. Guard dashboard
7. ADM dashboard
8. Security hardening
9. Docker Compose deployment
10. Vultr deployment
11. Monitoring
12. Backups
13. Future integrations: OAuth/Intra, QR, Telegram, SMS
