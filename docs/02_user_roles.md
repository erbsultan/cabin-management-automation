# 02 — User Roles

## Student

In MVP, students do not need direct access to the system.

Student actions:

- comes to the guard;
- shows 21 School/Intra profile;
- receives a key;
- returns a key.

Future student features:

- view personal trust score;
- view rental history;
- confirm key receiving through QR/OAuth/Telegram;
- receive return reminders.

## Guard

The guard can:

- issue a key;
- return a key;
- see active cabins;
- see timers;
- see grace/overdue status;
- add comments;
- add violations;
- mark “returned on time, but recorded later”.

The guard must not be able to:

- delete history;
- directly edit trust score;
- directly edit audit logs;
- change system settings;
- create ADM/admin users.

## ADM

ADM can:

- view live dashboard;
- view all cabin statuses;
- view history;
- view trust score;
- view violations;
- add violations;
- resolve disputed situations through audit-friendly actions;
- view analytics;
- control cabin rules.

ADM must not directly delete audit logs.

## Admin

Technical admin can:

- manage users;
- manage roles;
- manage cabin list;
- manage default time limits;
- manage grace period;
- manage deployment;
- configure backups;
- configure monitoring.
