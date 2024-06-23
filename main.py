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
        try : 
            df = pd.DataFrame({
                "Solar Angles" : ["Hour Angle",
                                "Declinition Angle",
                                "Solar Altitude Angle",
                                "Sunset Sunrise Angle",
                                "Zenith Angle",
                                "Solar Azimuth Angle"],
                "Calculated Values" : [f"{hour_angle(tm):.3f}°",
                                    f"{declinition_angle(dt):.3f}°",
                                    f"{solar_altitude_angle(latitude,tm,dt):.3f}°",
                                    f"{sunset_sunrise_angle(latitude,dt):.3f}°",
                                    f"{zenith_angle(latitude,tm,dt):.3f}°",
                                    f"{solar_azimuth_angle(latitude,tm,dt):.3f}°"]
                })
            st.table(df)
        except Exception as e: 
            print(Exception)
            st.warning("Some calculated angles are out of domain. Please use appropriate value of latitude.")
else : 
    if button: 
        st.warning("Please fill in all the fields before submission")
