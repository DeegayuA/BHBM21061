#!/usr/bin/env python3
"""
Create (or open) data/portfolio.db and insert two sample projects for the portfolio.

Run this script from the repository (or directly):
  python3 scripts/add_portfolio_projects.py

The DB file will be created at ./data/portfolio.db
"""
import os
import sqlite3

ROOT = os.path.dirname(os.path.dirname(__file__))
DB_DIR = os.path.join(ROOT, "data")
DB_PATH = os.path.join(DB_DIR, "portfolio.db")

os.makedirs(DB_DIR, exist_ok=True)

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

cur.execute(
    """
    CREATE TABLE IF NOT EXISTS projects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        url TEXT,
        tech TEXT,
        date TEXT
    );
    """
)

# Two sample projects to insert. Edit these as needed.
projects = [
    (
        "TaskTracker",
        "A lightweight task tracking web app with user auth and drag-and-drop tasks.",
        "https://example.com/tasktracker",
        "Python,Flask,SQLite,HTMX",
        "2024-08",
    ),
    (
        "PortfolioSite",
        "Personal portfolio site with blog, projects gallery and contact form.",
        "https://example.com/portfolio",
        "HTML,CSS,PHP,SQLite",
        "2025-06",
    ),
]

for title, description, url, tech, date in projects:
    cur.execute("SELECT id FROM projects WHERE title = ?", (title,))
    if cur.fetchone():
        print(f"Skipping existing project: {title}")
    else:
        cur.execute(
            "INSERT INTO projects (title, description, url, tech, date) VALUES (?,?,?,?,?)",
            (title, description, url, tech, date),
        )
        print(f"Inserted project: {title}")

conn.commit()
conn.close()

print("Done. Database written to:", DB_PATH)
