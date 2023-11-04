import json
import pandas as pd
import os
import folium
from folium import Choropleth, Circle, Marker, Icon, Map
from folium.plugins import HeatMap, MarkerCluster


def crear_mapa (city_lat,city_lon, df,zoom = 7):
   
    mapa = Map(location= [city_lat,city_lon], zoom_start = zoom)
    
    for index, row in df.iterrows():
        lat_c = row["lat"]
        lon_c= row["lon"]
        
        icon = Icon (
        icon = "fa-flag",
        prefix = "fa",
        color = "white",
        
        icon_color = "black")
        
        new_marker = Marker(location = [lat_c, lon_c], icon=icon)
        
        new_marker.add_to(mapa)
    icon = Icon (
    icon = "fa-flag",
    prefix = "fa",
    color = "white",
    icon_color = "red")
    new_marker = Marker(location = [city_lat, city_lon], icon=icon)
    new_marker.add_to(mapa)
    return mapa