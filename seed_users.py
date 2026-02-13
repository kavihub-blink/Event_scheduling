import sqlite3

conn = sqlite3.connect("event_system.db")
c = conn.cursor()

users = [
("coordinator","EventCoordinator","CSE","123"),
("hod","HOD","CSE","123"),
("dean","Dean","Engineering","123"),
("head","InstitutionalHead","Admin","123"),
("admin","Admin","System","123")
]

for u in users:
    c.execute("INSERT INTO users(name,role,department,password) VALUES(?,?,?,?)", u)

conn.commit()
conn.close()
print("Users added")
