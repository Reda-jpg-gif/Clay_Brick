
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Data for each additive mix
data = {
    "Additive": [
        "Raw clay", "Cork (13%)", "Quicklime", "Wool fibres", "Almond husk (15%)",
        "Typha (20%)", "Dry grass (15%)", "Bentonite (12%)", "Wood ash (10%)",
        "Olive ash (10%)", "OPBA (20%)"
    ],
    "Thermal Conductivity (W/m·K)": [0.721, 0.326, 0.490, 0.420, 0.552, 0.292, 0.338, 0.659, 0.484, 0.457, 0.430],
    "Compressive Strength (MPa)": [2.1, 3.4, 4.8, 3.7, 2.9, 3.2, 2.8, 3.6, 3.1, 3.3, 3.5],
    "Water Absorption (%)": [24.2, 18.5, 20.1, 19.3, 22.0, 17.4, 18.9, 23.8, 19.5, 20.3, 19.0],
    "CO2 Emissions (kg/m³)": [104, 82, 130, 121, 92, 75, 80, 110, 90, 88, 85],
    "Embodied Energy (MJ/m³)": [1040, 1180, 1536, 1600, 1120, 1020, 1080, 1360, 1056, 1048, 1040],
    "Cost (MAD/m³)": [0, 832, 288, 1600, 120, 96, 48, 288, 16, 16, 32],
    "Payback Period (years)": [float("inf"), 0.03, 0.18, 0.32, 0.06, 0.02, 0.02, 0.13, 0.05, 0.05, 0.04]
}

df = pd.DataFrame(data)

# Streamlit App
st.title("🧱 Clay + Additive Brick Performance Dashboard")
st.markdown("Analyze the strength, thermal, environmental, and cost performance of different clay + additive mixtures.")

# Selection
additive = st.selectbox("Select an Additive Mix", df["Additive"])
selected = df[df["Additive"] == additive].squeeze()

# Metrics Display
st.subheader(f"📊 Performance Summary for: {additive}")
st.metric("Thermal Conductivity (W/m·K)", selected["Thermal Conductivity (W/m·K)"])
st.metric("Compressive Strength (MPa)", selected["Compressive Strength (MPa)"])
st.metric("Water Absorption (%)", selected["Water Absorption (%)"])
st.metric("CO₂ Emissions (kg/m³)", selected["CO2 Emissions (kg/m³)"])
st.metric("Embodied Energy (MJ/m³)", selected["Embodied Energy (MJ/m³)"])
st.metric("Cost (MAD/m³)", selected["Cost (MAD/m³)"])
st.metric("Payback Period (years)", f"{selected['Payback Period (years)']:.2f}" if selected["Payback Period (years)"] != float("inf") else "∞")

# Comparison chart
st.subheader("📈 Comparison Chart")
option = st.selectbox("Select Parameter to Compare All Additives", df.columns[1:])
fig, ax = plt.subplots(figsize=(10, 4))
bars = ax.bar(df["Additive"], df[option], color="steelblue")
plt.xticks(rotation=45, ha='right')
plt.ylabel(option)
st.pyplot(fig)
