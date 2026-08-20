# Task Manager System

A simple console-based task management application built for TechMaster
Academy — Phase 01 / Project 01.

## Goal

Build strong programming logic using Python by developing a console-based
Task Manager application that lets a user manage daily tasks.

## Features

- Add a new task
- View all tasks
- Update an existing task
- Delete a task
- Mark a task as completed

Tasks persist between runs — they are saved to `tasks.json` after every
change, so nothing is lost when the program closes and reopens.

## How it works

- Each task is stored as a dictionary: `{"id": 1, "title": "...", "completed": false}`
- All tasks are kept in one list in memory while the app runs
- `load_tasks()` reads `tasks.json` into that list on startup (starting
  with an empty list if the file doesn't exist yet or is corrupted)
- `save_tasks()` writes the list back to `tasks.json` after every add,
  update, delete, or complete action
- Input is validated: empty titles are rejected, non-numeric IDs are
  rejected, and IDs that don't exist are reported without crashing

## Requirements

- Python 3.8+ (no external packages needed — only the standard library)

## Running it

```bash
python main.py
```

Then choose an option from the menu (1-6) and follow the prompts.

## Project structure

```
task-manager/
├── main.py        # the whole application
├── tasks.json      # created automatically on first save
└── .gitignore
```

## Grading focus (per project brief)

| Area | Weight |
|---|---|
| Task Management Features | 35% |
| Python Fundamentals | 25% |
| Functions & Code Organization | 20% |
| File Handling | 20% |
