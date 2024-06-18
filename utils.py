import math

"""
Using the geometric correlations presented relations presented in this chapter, develop a computer  program (Matlab, C++ etc.) that estimates all solar angles according to the latitude, day of  year, time of the day, and slope of surface.
"""


date = 21
latitude = 10
time_of_day = "12:32 am"
surface_slope = 21

def n(date):
    pass

def hour_angle(time):
    time = time.split(":")
    hours = int(time[0])
    minutes = int(time[0])
    if hours > 12 : 
        return (-1)*(12-hours)*(60)*(0.25)
    return (hours-12)(60)(0.25)


def declinition_angle(date):
    return 23.45*math.sin(360*((284*n(date))/365))


def solar_altitude_angle(latitude,time,date):
    return math.asin((math.cos(latitude)*math.cos(hour_angle(time))*math.cos(declinition_angle(n(date))))+(math.sin(latitude)*math.sin(declinition_angle(n(date)))))


def sunset_sunrise_angle(latitude,date):
    return math.acos(-1*math.tan(declinition_angle(n(date)))*math.tan(latitude))


def zenith_angle(latitude,time,date):
    return 90 - solar_altitude_angle(latitude,time,date)


def solar_azimuth_angle(latitude,time,date):
    return math.asin((math.cos(declinition_angle(n(date)))*math.sin(hour_angle(time)))/math.cos(solar_altitude_angle(latitude,time,date)))


def angle_of_incidence(latitude,time,date,surface_slope):
    pass
