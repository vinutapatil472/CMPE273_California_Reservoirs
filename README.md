# CMPE273_California_Reservoirs

# 💧 California Reservoir Monitoring Dashboard


This project is a **real-time interactive dashboard** built using **Python**, **Streamlit**, and **Plotly**, designed to **visualize and monitor water elevation levels** across major **California reservoirs** over the past 5 years.

## 🔁 Real-Time MQTT Integration

Each reservoir is treated as an individual **MQTT topic** (e.g., `reservoir/SHA`, `reservoir/ORO`, etc.).

- A **publisher** script simulates real-time data by streaming historical elevation values from CSV files to respective MQTT topics.
- A **subscriber** script listens to these topics and stores the incoming data in an SQLite database.
- This architecture mimics a real-world **IoT pipeline**, enabling the dashboard to reflect **live data ingestion**.

## 🚀 Features

- 📍 **Reservoir Selector** – Choose from 10 major reservoirs:
  - Shasta Lake (SHA), Oroville (ORO), Clear Lake (CLE), New Melones (NML), San Luis (SNL), Don Pedro (DNP), Berryessa (BER), Folsom (FOL), Bullards Bar (BUL), Pine Flat (PNF)
  
- 📈 **Elevation Trend Graph** – Interactive time series plot with a customizable date slider

- 📊 **Elevation Summary**
  - Min & Max Elevation for Selected Date Range
  - Min & Max Elevation for 5-Year Data

- 🗺️ **California Map Integration**
  - Reservoirs plotted on a Mapbox-powered California state map
  - The selected reservoir is highlighted in **red**, others in **grey/white**

- 🔄 **Real-Time Simulation** (Optional)
  - Simulated publisher & subscriber setup using MQTT (paho-mqtt)
  - Data stored in a local SQLite database






## 🧪 Tech Stack

- `Python 3.x`
- `Streamlit`
- `Plotly`
- `pandas`
- `paho-mqtt`
- `SQLite3`
- `Mapbox`

---

## 🛠️ Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/ca-reservoir-dashboard.git
   cd ca-reservoir-dashboard
