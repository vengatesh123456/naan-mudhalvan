# urban_planning_app.py
import streamlit as st
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

st.title("Smart Urban Planning Simulation")

zone_type = st.sidebar.selectbox("Choose zone type", ["Residential", "Commercial", "Industrial", "Mixed Use"])
population_growth = st.sidebar.slider("Estimated Population Growth (%)", 0, 100, 20)
green_space_addition = st.sidebar.slider("Green Space Increase (%)", 0, 50, 10)

data = {
    'Zone': ['Zone A', 'Zone B', 'Zone C'],
    'Type': ['Residential', 'Commercial', 'Industrial'],
    'Population': [5000, 2000, 1000],
    'Green_Space (%)': [10, 5, 2]
}
df = pd.DataFrame(data)
