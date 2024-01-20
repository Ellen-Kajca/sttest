import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Load the data
@st.cache_data
def load_data():
    data = pd.read_csv("/Users/ellenkajca/Documents/streamlitTest/NY-House-Dataset.csv")
    return data

data = load_data()

# Sidebar Filters
st.sidebar.header("Filter Options")
# Add filters here. Example:
price_range = st.sidebar.slider("Price Range", min_value=int(data["PRICE"].min()), max_value=int(data["PRICE"].max()), value=(int(data["PRICE"].min()), int(data["PRICE"].max())))

# Filter the data
filtered_data = data[(data["PRICE"] >= price_range[0]) & (data["PRICE"] <= price_range[1])]

# Display data table
st.write("Displaying Property Data")
st.dataframe(filtered_data)

# Visualizations
# Price Distribution
st.write("Price Distribution")
fig = px.histogram(filtered_data, x="PRICE")
st.plotly_chart(fig)

# Map of Properties
st.write("Map of Properties")
fig = px.scatter_mapbox(filtered_data, lat="LATITUDE", lon="LONGITUDE", hover_name="ADDRESS", hover_data=["PRICE", "BEDS", "BATH"], zoom=10, height=300)
fig.update_layout(mapbox_style="open-street-map")
st.plotly_chart(fig)
