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

def city_map(df):
    mapa = folium.Map(location= [51.51689597746479, -0.1473155197183098], zoom_start = 15)
    folium.Marker([51.51689597746479, -0.1473155197183098],
    popup='MY_COMPANY',
    icon=folium.Icon(color='red', icon = 'info-sign'),
    z_index_offset=1000).add_to(mapa)

    category_colors = {
    'karaoke': 'purple',
    'bar': 'purple',
    'starbucks': 'green',
    'veganrestaurant': 'orange',
    'elementaryschool': 'lightblue',
    'middleschool': 'lightblue',
    'web': 'black',
    'games_video': 'black',
    'petgrooming ': 'lightred'
}
# Add markers for the venues
    for idx, row in df.iterrows():
        folium.Marker(
            [row['lat'], row['lon']],
            popup=f"{row['name']} ({row['category']})",
            icon=folium.Icon(color=category_colors.get(row['category'], 'gray'))
        ).add_to(mapa)
    return mapa