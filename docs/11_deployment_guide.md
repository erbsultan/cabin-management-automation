# 11 — Deployment Guide

## Phase 1: Local Repository Setup

```bash
mkdir -p cabins-management-system/{docs,frontend,backend,infra,scripts,.github/workflows}
cd cabins-management-system

git init -b main

touch README.md .gitignore .env.example docker-compose.yml
```

## Phase 2: Add Documentation

Put all documentation files into:

```text
docs/
```

Then commit:

```bash
git add .
git commit -m "Initialize project documentation and repository structure"
```

## Phase 3: Create GitHub Repository

Recommended repository name:

```text
cabins-management-system
```

Then connect local repo:

```bash
git remote add origin git@github.com:<your-username>/cabins-management-system.git
git push -u origin main
```

## Phase 4: Local Development Later

Later we will add:

- backend;
- frontend;
- database;
- Docker Compose.

## Phase 5: Vultr Deployment Later

Planned steps:

1. Create Vultr VPS.
2. Choose region after latency test.
3. Install Ubuntu 24.04.
4. Configure SSH keys.
5. Configure UFW.
6. Install Docker and Docker Compose.
7. Clone repository.
8. Create production `.env`.
9. Start services.
10. Configure domain.
11. Configure HTTPS.
12. Check `/health`.
13. Check dashboard.
14. Check backup.
15. Check monitoring.
