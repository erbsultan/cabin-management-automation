# 10 — Backup and Restore

## Backup Goal

If the server breaks, database is damaged, or someone makes a mistake, we must be able to restore the system.

## Minimum Backup Strategy

1. Daily PostgreSQL dump.
2. Keep backups for 7–14 days.
3. Do not store backups only on the same server.
4. Periodically test restore.

## Important Rule

Backup without restore test is not a real backup.

## Planned Script

Location:

```text
scripts/backup_db.sh
```

The script will later:

- read database credentials from environment;
- create a timestamped dump;
- compress it;
- optionally upload it to external storage.

## Planned Restore Script

Location:

```text
scripts/restore_db.sh
```

The script will later:

- take a backup file;
- restore it into PostgreSQL;
- verify that the database is usable.

## Sensitive Data

Backups may contain personal and operational data.

Backups must not be committed to Git.

`.gitignore` already contains:

```gitignore
*.dump
*.sql
```
