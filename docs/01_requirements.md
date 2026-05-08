# 01 — Requirements

## Functional Requirements

### Key Issue

The guard must be able to:

- enter student login;
- optionally enter student full name;
- select a cabin;
- select a rental time limit;
- add an optional comment;
- start the rental.

### Key Return

The guard must be able to:

- see active rentals;
- open a rental;
- mark the key as returned;
- mark “returned on time, but recorded later”;
- add a comment;
- finish the rental.

### Dashboard

The system must show:

- free cabins;
- occupied cabins;
- student login inside each active cabin;
- remaining time;
- grace period status;
- overdue status;
- violations;
- trust score changes.

### History

The system must store:

- who took a key;
- which cabin was used;
- who issued the key;
- when it was issued;
- what time limit was set;
- when it should have been returned;
- when it was actually returned;
- whether it was returned on time;
- whether it entered grace period;
- whether it was overdue;
- comments;
- violations.

### Violations

The system must allow guard or ADM to record violations such as:

- eating in the cabin;
- noise;
- non-study activity;
- abuse of cabin usage;
- disturbing others;
- late return;
- exceeding time limit;
- other violation with comment.

### Trust Score

The system must calculate student trust score from trust events.

Trust score must not be manually edited directly.

## Non-Functional Requirements

The system should be:

- simple to use;
- secure by design;
- auditable;
- deployable on VPS;
- easy to update later;
- monitorable;
- backup-friendly;
- understandable for a Junior/Middle DevOps portfolio.

## Out of Scope for MVP

Not included in the first version:

- Intra/OAuth verification;
- SMS verification;
- Telegram verification;
- QR confirmation;
- mobile application;
- automatic integration with 21 School database;
- complex analytics or ML.
