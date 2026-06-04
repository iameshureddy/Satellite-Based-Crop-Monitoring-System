import streamlit as st
import pandas as pd
from utils.sentinel_ndvi import get_ndvi
from utils.sentinel_ndvi_map import get_ndvi_map
from utils.sentinel_timeseries import ndvi_timeseries

df = pd.read_csv("data/fields.csv")
field = st.session_state["selected_field"]
row = df[df.field_name == field].iloc[0]

lat, lon = row.latitude, row.longitude

st.title(field)

ndvi = get_ndvi(lat, lon)
st.metric("NDVI", ndvi)

st.image(get_ndvi_map(lat, lon))

ts = ndvi_timeseries(lat, lon)
st.line_chart(ts.set_index("date")["NDVI"])
