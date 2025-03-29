import paho.mqtt.client as mqtt
import json
import sqlite3
import os

# ✅ Ensure DB and table exist before starting MQTT
DB_PATH = "reservoir.db"

def init_db():
    if not os.path.exists(DB_PATH):
        open(DB_PATH, "w").close()

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS reservoir_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            station_id TEXT,
            date TEXT,
            elevation REAL
        )
    ''')
    conn.commit()
    conn.close()

init_db()  # 🧠 Call once before MQTT starts

# ✅ Now connect DB for ongoing use
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# ✅ MQTT message handler
def on_message(client, userdata, msg):
    try:
        payload = json.loads(msg.payload.decode())
        station_id = payload["station_id"]
        date = payload["date"]
        elevation = float(payload["elevation"])

        print(f"📥 Received from {msg.topic}: {payload}")

        cursor.execute('''
            INSERT INTO reservoir_data (station_id, date, elevation)
            VALUES (?, ?, ?)
        ''', (station_id, date, elevation))
        conn.commit()

    except Exception as e:
        print(f"[!] Error processing message: {e}")

# ✅ MQTT connection
client = mqtt.Client()
client.on_message = on_message
client.connect("localhost", 1883, 60)

# ✅ Subscribe to all reservoirs
station_ids = ["SHA", "ORO", "CLE", "NML", "SNL", "DNP", "BER", "FOL", "BUL", "PNF"]
for station_id in station_ids:
    client.subscribe(f"reservoir/{station_id}")

print("🛰️ Listening for live reservoir data and storing in DB...")
client.loop_forever()

