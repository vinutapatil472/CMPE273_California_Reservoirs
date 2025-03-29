import streamlit as st
import pandas as pd
import plotly.express as px
import os
from datetime import datetime

# Configure Streamlit page
st.set_page_config(page_title="California Reservoir Levels", layout="wide")

st.markdown("""
    <h1 style='text-align: center;'>💧 California Reservoir Levels Dashboard</h1>
""", unsafe_allow_html=True)

# 📍 Reservoir Metadata (coordinates for mapping)
reservoir_info = {
    "SHA": {"name": "Shasta Lake", "lat": 40.7890, "lon": -122.2976},
    "ORO": {"name": "Lake Oroville", "lat": 39.5625, "lon": -121.4513},
    "CLE": {"name": "Clear Lake", "lat": 41.8600, "lon": -121.1460},
    "NML": {"name": "New Melones", "lat": 37.9879, "lon": -120.5355},
    "SNL": {"name": "San Luis Reservoir", "lat": 37.0561, "lon": -121.1138},
    "DNP": {"name": "Don Pedro Reservoir", "lat": 37.7354, "lon": -120.3839},
    "BER": {"name": "Berryessa Lake", "lat": 38.6097, "lon": -122.2540},
    "FOL": {"name": "Folsom Lake", "lat": 38.7292, "lon": -121.1195},
    "BUL": {"name": "New Bullards Bar", "lat": 39.4395, "lon": -121.1338},
    "PNF": {"name": "Pine Flat Lake", "lat": 36.8603, "lon": -119.2873},
}

station_id = st.selectbox("Select a Reservoir Station:", sorted(reservoir_info.keys()))

csv_path = f"data/sample_data_{station_id}.csv"

if not os.path.exists(csv_path):
    st.error("Data not found for this station.")
else:
    df = pd.read_csv(csv_path)

    # Clean and preprocess
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df["elevation"] = pd.to_numeric(df["elevation"], errors="coerce")
    df = df[df["elevation"].notna() & (df["elevation"] > -9999)]

    # Convert datetime to date for slider
    min_date = df["date"].min().date()
    max_date = df["date"].max().date()

    # Layout: Left (Controls + Graph) | Right (Map)
    left, right = st.columns([2, 1])

    with left:
        date_range = st.slider("Select date range:", min_value=min_date, max_value=max_date, value=(min_date, max_date))
        start_dt, end_dt = pd.to_datetime(date_range[0]), pd.to_datetime(date_range[1])
        filtered_df = df[(df["date"] >= start_dt) & (df["date"] <= end_dt)]

        st.subheader(f"📈 Elevation Trend: {reservoir_info[station_id]['name']}")
        fig = px.line(filtered_df, x="date", y="elevation", labels={"elevation": "Elevation (ft)", "date": "Date"},
                      title=f"Water Elevation Over Time ({station_id})")
        fig.update_layout(title_x=0.5)
        st.plotly_chart(fig, use_container_width=True)

        # Elevation stats
        range_min = filtered_df["elevation"].min()
        range_max = filtered_df["elevation"].max()
        full_min = df["elevation"].min()
        full_max = df["elevation"].max()

        st.subheader("📊 Elevation Summary")
        col1, col2 = st.columns(2)
        col1.metric("🔻 Min Elevation (Selected Range)", f"{range_min:.2f} ft")
        col2.metric("🔹 Max Elevation (Selected Range)", f"{range_max:.2f} ft")
        col1.metric("📉 Min Elevation (5 Years)", f"{full_min:.2f} ft")
        col2.metric("📈 Max Elevation (5 Years)", f"{full_max:.2f} ft")

    with right:
        st.subheader("🗺️ Reservoir Locations")
        map_df = pd.DataFrame.from_dict(reservoir_info, orient='index')
        map_df = map_df.reset_index().rename(columns={"index": "station"})
        map_df["color"] = map_df["station"].apply(lambda x: "red" if x == station_id else "lightgrey")
        map_df["size"] = map_df["station"].apply(lambda x: 18 if x == station_id else 10)

        fig_map = px.scatter_mapbox(
            map_df,
            lat="lat",
            lon="lon",
            hover_name="name",
            color="color",
            size="size",
            size_max=20,
            zoom=5.3,
            height=500,
            color_discrete_map="identity"
        )

        fig_map.update_layout(
            mapbox_style="carto-positron",
            margin={"r": 0, "t": 0, "l": 0, "b": 0},
            showlegend=False
        )

        st.plotly_chart(fig_map, use_container_width=True)
