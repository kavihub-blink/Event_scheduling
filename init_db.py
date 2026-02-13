import sqlite3

conn = sqlite3.connect("event_system.db")
cursor = conn.cursor()

schema = """
CREATE TABLE IF NOT EXISTS users(
 user_id INTEGER PRIMARY KEY AUTOINCREMENT,
 name TEXT,
 role TEXT,
 department TEXT,
 password TEXT
);

CREATE TABLE IF NOT EXISTS events(
 event_id INTEGER PRIMARY KEY AUTOINCREMENT,
 title TEXT,
 date TEXT,
 time TEXT,
 duration TEXT,
 participants INTEGER,
 status TEXT,
 created_by INTEGER
);

CREATE TABLE IF NOT EXISTS resources(
 resource_id INTEGER PRIMARY KEY AUTOINCREMENT,
 type TEXT,
 total_qty INTEGER,
 available_qty INTEGER
);

CREATE TABLE IF NOT EXISTS venues(
 venue_id INTEGER PRIMARY KEY AUTOINCREMENT,
 name TEXT,
 capacity INTEGER
);

CREATE TABLE IF NOT EXISTS allocations(
 allocation_id INTEGER PRIMARY KEY AUTOINCREMENT,
 event_id INTEGER,
 resource_id INTEGER,
 qty INTEGER,
 venue_id INTEGER,
 time_slot TEXT
);
"""

cursor.executescript(schema)
conn.commit()
conn.close()

print("Database created successfully")
