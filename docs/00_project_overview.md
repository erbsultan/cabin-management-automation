# 00 — Project Overview

## Project Name

**Cabin Management System**

A digital system for managing physical cabin keys in 21 School.

Inside this project we use the word **cabins**, not “skatnitsy”.

## Context

In 21 School, there are several cabins that students can use for studying. Access is controlled through physical keys. Currently, the process is manual: a student comes to a guard or ADM, receives a key, and the event is written down on paper.

The goal is to replace the paper journal with a digital system.

## Main Goal

Build a web-based system where guards and ADM can:

- issue cabin keys;
- return cabin keys;
- monitor active cabin usage;
- track time limits;
- track grace period;
- detect overdue rentals;
- record violations;
- see student responsibility history;
- calculate trust score;
- audit all important actions.

## Important MVP Decision

Automatic student verification through OAuth/Intra, SMS, Telegram, or QR is postponed.

For the first version:

1. The student comes to the guard.
2. The student shows their 21 School/Intra profile.
3. The guard manually checks the profile.
4. The guard manually enters the student's unique login.
5. The system starts tracking the rental.

## Why This Project Is Useful

For 21 School:

- less paper;
- more transparency;
- easier monitoring;
- better accountability.

For portfolio:

- real-world problem;
- backend logic;
- frontend dashboard;
- database modeling;
- security;
- DevOps deployment;
- monitoring;
- backups;
- CI/CD later.
