# 05 — Database Schema

## users

```text
id
username
password_hash
role
is_active
created_at
updated_at
```

Roles:

```text
guard
adm
admin
```

## students

```text
id
login
full_name optional
base_trust_score
created_at
updated_at
```

Important:

- `login` is the main student identifier.
- `full_name` is optional metadata.
- Trust score should be calculated from events, not edited directly.

## cabins

```text
id
number
name
is_active
created_at
updated_at
```

## rentals

```text
id
student_login
cabin_id
issued_by_user_id
returned_by_user_id
started_at
due_at
grace_until
returned_at
status
result
comment
created_at
updated_at
```

Possible status values:

```text
ACTIVE
GRACE
OVERDUE
RETURNED
CANCELLED
```

Possible result values:

```text
returned_on_time
returned_in_grace
returned_late
returned_on_time_manual_override
cancelled
```

## violations

```text
id
rental_id
student_login
type
comment
created_by_user_id
created_at
```

Violation types:

```text
late_return
exceeded_limit
food
noise
non_study_activity
abuse_cabin
disturbing_others
other
```

## trust_events

```text
id
student_login
rental_id
points_change
reason
created_by_user_id
created_at
```

Trust score formula:

```text
trust_score = base_trust_score + sum(trust_events.points_change)
```

## audit_logs

```text
id
actor_user_id
action
entity_type
entity_id
old_value
new_value
ip_address
user_agent
comment
created_at
```

Audit log examples:

```text
guard_01 issued cabin_3 to esultan
guard_01 returned rental_15
adm_02 added violation to rental_15
admin changed grace period from 5 to 7 minutes
```
