# 13 — Next Steps

## Current Status

We have finished the idea and planning stage.

Next step: create the repository foundation.

## Step 1 — Create Local Folder

```bash
mkdir -p ~/cabins-management-system
cd ~/cabins-management-system
```

Alternative inside existing portfolio:

```bash
mkdir -p ~/devops-portfolio/apps/cabins-management-system
cd ~/devops-portfolio/apps/cabins-management-system
```

## Step 2 — Initialize Git

```bash
git init -b main
```

## Step 3 — Add Files

Copy the generated files into the repository:

```text
README.md
.gitignore
.env.example
docker-compose.yml
docs/
frontend/
backend/
infra/
scripts/
.github/workflows/
```

## Step 4 — First Commit

```bash
git add .
git commit -m "Initialize Cabin Management System documentation"
```

## Step 5 — Create GitHub Repository

Suggested repo name:

```text
cabins-management-system
```

## Step 6 — Push to GitHub

```bash
git remote add origin git@github.com:<your-username>/cabins-management-system.git
git push -u origin main
```

## Step 7 — Next Practical Milestone

After repository is ready, build the backend skeleton:

```text
FastAPI + PostgreSQL + /health + database migrations
```

Expected result:

- backend starts locally;
- PostgreSQL starts locally;
- `/health` returns ok;
- first migration exists;
- everything is committed.
