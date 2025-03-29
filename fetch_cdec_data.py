import requests
import pandas as pd
import os

os.makedirs("data", exist_ok=True)

def fetch_and_save(station_id):
    url = "https://cdec.water.ca.gov/dynamicapp/req/JSONDataServlet"
    params = {
        "Stations": station_id,
        "SensorNums": "6",
        "dur_code": "D",
        "Start": "2020-01-01",
        "End": "2025-03-28"
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()

        if not isinstance(data, list) or len(data) == 0:
            print(f"[✗] No data for {station_id}")
            return

        df = pd.DataFrame(data)
        df = df[["date", "value"]].dropna()
        df.columns = ["date", "elevation"]
        df["elevation"] = pd.to_numeric(df["elevation"], errors="coerce")
        df.dropna(inplace=True)

        df.to_csv(f"data/sample_data_{station_id}.csv", index=False)
        print(f"[✓] {station_id}: Saved {len(df)} rows")

    except Exception as e:
        print(f"[!] Error fetching {station_id}: {e}")

stations = ["SHA", "ORO", "CLE", "NML", "SNL", "DNP", "BER", "FOL", "BUL", "PNF"]

for sid in stations:
    fetch_and_save(sid)

