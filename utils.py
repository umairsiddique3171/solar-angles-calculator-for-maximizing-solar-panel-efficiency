import math
import time
import datetime
import streamlit as st
import base64

latitude = 10
tm = "23:30:00"
dt = "2014-07-16"

def n(dt):
    dt = str(dt)
    dt = dt.split("-")
    if ('0' in dt[1]) or ('0' in dt[2]):
        y,m,d = int(dt[0]),int(dt[1][1:]),int(dt[1][1:])
    else:
        y,m,d = int(dt[0]),int(dt[1]),int(dt[2])
    dt = datetime.date(y,m,d)
    return int(dt.timetuple().tm_yday)

def hour_angle(tm):
    tm = str(tm)
    tm = tm.split(":")
    hours = int(tm[0])
    minutes = int(tm[1])
    if hours > 12 : 
        return ((hours-12)*(60) + minutes)*(0.25)
    return ((12-hours)*(60) - minutes)*(60)*(0.25)

def declinition_angle(dt):
    return 23.45*math.sin(360*((284*n(dt))/365))

def solar_altitude_angle(latitude,tm,dt):
    return math.asin((math.cos(latitude)*math.cos(hour_angle(tm))*math.cos(declinition_angle(dt)))+(math.sin(latitude)*math.sin(declinition_angle(dt))))

def sunset_sunrise_angle(latitude,dt):
    return math.acos(-1*math.tan(declinition_angle(dt))*math.tan(latitude))

def zenith_angle(latitude,tm,dt):
    return 90 - solar_altitude_angle(latitude,tm,dt)

def solar_azimuth_angle(latitude,tm,dt):
    return math.asin((math.cos(declinition_angle(dt))*math.sin(hour_angle(tm)))/math.cos(solar_altitude_angle(latitude,tm,dt)))

def set_background(img_file):

    with open(img_file, "rb") as f:
        img_data = f.read()
    b64_encoded = base64.b64encode(img_data).decode()
    style = f"""
        <style>
        .stApp {{
            background-image: url(data:image/png;base64,{b64_encoded});
            background-size: cover;
        }}
        </style>
    """
    st.markdown(style, unsafe_allow_html=True)