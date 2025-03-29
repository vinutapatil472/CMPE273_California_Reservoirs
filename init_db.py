import sqlite3

conn = sqlite3.connect("reservoir.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS reservoir_data (
        station_id TEXT,
        date TEXT,
        elevation REAL
    )
''')

conn.commit()
conn.close()

print("✅ Table created successfully.")

