# 03 — Business Flow

## Key Issue Flow

```text
Student
  ↓
Shows 21 School/Intra profile
  ↓
Guard manually checks profile
  ↓
Guard enters student login
  ↓
Guard selects cabin
  ↓
Guard selects time limit
  ↓
Guard clicks “Issue Key”
  ↓
Backend creates rental
  ↓
Timer starts
  ↓
ADM dashboard updates
```

## Key Return Flow

```text
Student returns key
  ↓
Guard opens active rental
  ↓
Guard clicks “Returned”
  ↓
Backend checks server time
  ↓
Backend calculates result
  ↓
Rental status becomes RETURNED
  ↓
Trust event is created
  ↓
Audit log is created
```

## Manual Return Override

Sometimes the student may return the key on time, but the guard records it later.

For this case, the guard can use:

```text
“Returned on time, but recorded later”
```

This should:

- finish the rental;
- avoid unfair trust score penalty;
- create audit log;
- optionally require comment in a later version.

## Rental Statuses

```text
FREE      — cabin is free
ACTIVE    — cabin is occupied and still within time limit
GRACE     — main time limit is over, but grace period is active
OVERDUE   — grace period is over, rental is late
RETURNED  — key was returned
CANCELLED — rental was cancelled due to mistake
```

## Time Logic Example

```text
Rental limit: 60 minutes
Grace period: 5 minutes
```

Result:

```text
0–60 minutes      ACTIVE
60–65 minutes     GRACE
65+ minutes       OVERDUE
```

## Important Rule

The timer must be calculated on the backend using server time.

Frontend only displays the countdown.
