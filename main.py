import numpy as np
import pandas as pd 
import streamlit as st
from utils import *

st.set_page_config(page_title="Solar Angles Calculator", page_icon="☀️")

set_background("background_img.jpg")

st.markdown("""
<style>
.stDeployButton
{
    visibility : hidden;
}
.st-emotion-cache-czk5ss.e16jpq800
{
    visibility : hidden;
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    """
    <div style="text-align: center;">
        <h1>Solar Angles Calculator</h1>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

col1,col2 = st.columns(2)
with col1: 
    dt = st.date_input("Enter Date")
with col2: 
    tm = st.time_input("Enter Time")
with col1:
    latitude = st.number_input("Enter Latitude Coordinates", min_value = -90.0, max_value= 90.0, step=0.1) 

button = st.button('Submit')

if dt and tm and latitude is not None: 
    if button: 
        st.success("Submitted Successfully")
        st.markdown("---")
        df = pd.DataFrame({
            "Hour Angle":f"{hour_angle(tm)}°",
            "Declinition Angle":f"{declinition_angle(dt)}°",
            "Solar Altitude Angle":f"{solar_altitude_angle(latitude,tm,dt)}°",
            "Sunset Sunrise Angle":f"{sunset_sunrise_angle(latitude,dt)}°",
            "Zenith Angle":f"{zenith_angle(latitude,tm,dt)}°",
            "Solar Azimuth Angle":f"{solar_azimuth_angle(latitude,tm,dt)}°"
            })
        st.table(df)
else : 
    if button: 
        st.warning("Please fill in all the fields before submission")
