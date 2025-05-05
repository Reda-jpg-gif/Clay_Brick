
import streamlit as st
import pandas as pd

# Mixture data
data = {
    'Clay': {'cost_per_kg': 0.30, 'lambda': 0.40, 'co2': 0.050, 'strength': 19.49},
    'Clay + Straw': {'cost_per_kg': 0.29, 'lambda': 0.05, 'co2': 0.046, 'strength': 16.37},
    'Clay + Sawdust': {'cost_per_kg': 0.28, 'lambda': 0.055, 'co2': 0.047, 'strength': 15.59},
    'Clay + Rice Husk': {'cost_per_kg': 0.285, 'lambda': 0.065, 'co2': 0.047, 'strength': 15.59},
    'Clay + Fly Ash': {'cost_per_kg': 0.288, 'lambda': 0.09, 'co2': 0.048, 'strength': 15.20},
    'Clay + Hemp Fiber': {'cost_per_kg': 0.33, 'lambda': 0.06, 'co2': 0.046, 'strength': 14.62},
    'Clay + Lime': {'cost_per_kg': 0.39, 'lambda': 0.11, 'co2': 0.120, 'strength': 16.18}
}

st.title("Clay Brick Mixture Analysis Dashboard")

# User inputs
mixture = st.selectbox("Select a Mixture:", list(data.keys()))
additive_percent = st.slider("Additive Percentage (for info only)", 0, 50, 10)
thickness = st.slider("Wall Thickness (m)", 0.05, 0.5, 0.10)
area = st.number_input("Wall Area (m²)", min_value=1.0, value=10.0)
density = 1700  # kg/m³
carbon_price = 1.0  # MAD/kg CO2

# Extract data
d = data[mixture]
cost_per_kg = d['cost_per_kg']
lambda_val = d['lambda']
co2 = d['co2']
strength = d['strength']

# Calculations
volume = area * thickness
mass = density * volume
cost = cost_per_kg * mass
R_value = thickness / lambda_val
co2_total = co2 * mass
co2_penalty = co2_total * carbon_price

# Display results
st.subheader("Calculated Outputs")
st.write(f"**Material Cost:** {cost:.2f} MAD")
st.write(f"**Thermal Resistance (R-value):** {R_value:.2f} m²·K/W")
st.write(f"**Compressive Strength:** {strength:.2f} MPa")
st.write(f"**CO₂ Emissions:** {co2_total:.2f} kg")
st.write(f"**Carbon Cost Penalty:** {co2_penalty:.2f} MAD")
