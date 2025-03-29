# CMPE273_California_Reservoirs

# 💧 California Reservoir Monitoring Dashboard


This project is a **real-time interactive dashboard** built using **Python**, **Streamlit**, and **Plotly**, designed to **visualize and monitor water elevation levels** across major **California reservoirs** over the past 5 years.

## 👥 Team Members

| Name                | SJSU ID     |
|---------------------|-------------|
| Abhinav Sriharsha   | 017514900   |
| Vinuta Patil        | 018196035   |
| Bhavika Sodagum     | 017506567   |
| Ravi Teja Gattu     | 017503746   |

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
    
### Reservoirs Covered

| Reservoir Name         | Code |
|------------------------|------|
| Shasta Lake            | SHA  |
| Lake Oroville          | ORO  |
| Clear Lake             | CLE  |
| New Melones            | NML  |
| San Luis Reservoir     | SNL  |
| Don Pedro Reservoir    | DNP  |
| Berryessa Lake         | BER  |
| Folsom Lake            | FOL  |
| New Bullards Bar       | BUL  |
| Pine Flat Lake         | PNF  |






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

**Step 1: Activate virtual environment**  
```bash
source venv/bin/activate
```
**Step 2: Start the publisher**  
```bash
python3 publisher.py
```
**Step 3: Start the subscriber**  
```bash
python3 subscriber.py
```
**Step 4: Run the Streamlit dashboard**  
```bash
streamlit run dashboard.py
```
**Step 5: Visit the dashboard in your browser**  
```bash
http://localhost:8501
```

## 📊 Dashboard Preview

<img src="https://github.com/vinutapatil472/CMPE273_California_Reservoirs/blob/main/assets/Screenshot%202025-03-28%20at%208.27.41%E2%80%AFPM.png" width="600"/>

## Dropdown

<img src="https://github.com/vinutapatil472/CMPE273_California_Reservoirs/blob/main/assets/Screenshot%202025-03-28%20at%208.28.04%E2%80%AFPM.png" width="600"/>


### 🔍 Dashboard Features

- **🔽 Dropdown Menu**: Select any one of the 10 California reservoirs.
- **📅 Date Range Slider**: Choose a custom time window to explore trends.
- **📈 Line Graph (Plotly)**: Visualizes water elevation over time interactively.
- **📊 Metrics Panel**:
  - Minimum and maximum elevation for the selected date range.
  - Minimum and maximum elevation across full 5-year dataset.
- **🗺️ California Reservoir Map**:
  - Selected reservoir is highlighted in **red**.
  - All other reservoirs shown in **grey**.
  - Zoomable and hoverable for better spatial context.

