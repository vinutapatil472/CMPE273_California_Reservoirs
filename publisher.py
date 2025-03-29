import os
import time
import json
import pandas as pd
import paho.mqtt.client as mqtt

# MQTT setup
broker_address = "localhost"
topic_prefix = "reservoir"

client = mqtt.Client()
client.connect(broker_address, 1883, 60)

# Folder where all your CSVs are stored
data_folder = "data"
csv_files = [f for f in os.listdir(data_folder) if f.startswith("sample_data_") and f.endswith(".csv")]

for file in csv_files:
    station_id = file.replace("sample_data_", "").replace(".csv", "")
    filepath = os.path.join(data_folder, file)
    df = pd.read_csv(filepath)

    # Normalize column names like "DATE", "RES ELE FEET"
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

    # Rename columns if necessary
    if "res_ele_feet" in df.columns:
        df.rename(columns={"res_ele_feet": "elevation"}, inplace=True)
    if "date" not in df.columns or "elevation" not in df.columns:
        print(f"[!] Skipping {station_id}: Missing expected columns.")
        continue

    # Filter rows where elevation is a number
    df = df[df["elevation"].apply(lambda x: str(x).replace(".", "", 1).isdigit())]

    print(f"\n🌊 Streaming: {station_id}")
    for _, row in df.iterrows():
        payload = {
            "station_id": station_id,
            "date": row["date"],
            "elevation": float(row["elevation"])
        }
        client.publish(f"{topic_prefix}/{station_id}", json.dumps(payload))
        print(f"Published to {topic_prefix}/{station_id}: {payload}")
        time.sleep(1)  # simulate real-time streaming

print("\n✅ All reservoir data published.")

