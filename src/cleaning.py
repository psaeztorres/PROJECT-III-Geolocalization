import requests
import os
import pandas as pd
from geopy.distance import great_circle

def merge_and_get_top10_cities(df1,df2):
    result = pd.merge(df1, df2, on=None, how='outer')
    result.drop(['number_of_employees','founded_year','total_money_raised','lon', "lat"],axis=1, inplace=True)
    result = result.dropna(subset=['city1'])
 
    result['city1'] = result['city1'].str.strip()
    result['city2'] = result['city2'].str.strip()
 
    combined_cities = pd.concat([result['city1'], result['city2']], ignore_index=True).dropna()
 
    cities = combined_cities.value_counts().head(10).reset_index()
    cities.columns = ['City','Count']
    cities = cities[cities['City'].notna()]
    cities = cities[cities['City'] != '']
    return cities

def top10_cities(df):
    
    df.drop(['number_of_employees','founded_year','total_money_raised','lon', "lat"],axis=1, inplace=True)
    df = df.dropna(subset=['city1'])
    combined_cities = pd.concat([df['city1'], df['city2']], ignore_index=True).dropna()
    cities = combined_cities.value_counts().head(10)
   
    return cities


def merge_cities(df1, df2):
    # Merge DataFrames based on 'name' and 'City'
    merged_df = df1.merge(df2, on=['City'], how='inner', suffixes=('_startups', '_comp'))
    
    # Rename the 'Count' columns to 'Count_startups' and 'Count_comp'
    merged_df.rename(columns={'Count_startups': 'Count_startups', 'Count_comp': 'Count_comp'}, inplace=True)
    
    return merged_df


def clean_coord (df, city_lat, city_lon,radius=75):
    city_coords = (city_lat, city_lon)
    def is_within_radius(row,  city_lat, city_lon, radius_km=radius):
        point_coords = (row['lat'], row['lon'])
        
        distance = great_circle(city_coords, point_coords).kilometers
        return distance <= radius_km

    # Filtrar el DataFrame para mantener solo los puntos dentro del radio
    filtered_df = df[df.apply(is_within_radius, axis=1, args=(city_coords, radius))]

    return filtered_df





def get_avg_coordinates (city,city_lat, city_lon, *df):
    result = pd.concat(list(df), axis=0, ignore_index=True)
    result.drop(['number_of_employees','founded_year','total_money_raised','city2'],axis=1, inplace=True)
    result = result.dropna(subset=['city1'])
    result = result.dropna(subset=['lat'])
    result = result.dropna(subset=['lon'])
    result = result[result['city1'] == city]
    result['city1'] = result['city1'].str.strip()
    result = clean_coord (result, city_lat, city_lon,radius=75)
    avg_lat= result['lat'].mean()
    avg_lon= result['lon'].mean()
    return (avg_lat,avg_lon)








def df_city_coordinates (city,city_lat, city_lon, *df):
    result = pd.concat(list(df), axis=0, ignore_index=True)
    result.drop(['number_of_employees','founded_year','total_money_raised','city2'],axis=1, inplace=True)
    result = result.dropna(subset=['city1'])
    result = result.dropna(subset=['lat'])
    result = result.dropna(subset=['lon'])
    result = result[result['city1'] == city]
    result['city1'] = result['city1'].str.strip()
    result = clean_coord (result, city_lat, city_lon,radius=100)
    return result


def distance_venue_city (lista, df):
    df['category'] = df['category'].replace({'Elementary School': 'school', 'Middle School': 'school'})
    missing_categories = [cat for cat in lista if cat not in df['category'].unique()]

    if not missing_categories:
        # Calculate the average distance for each category
        avg_distance = df.groupby('category')['distance'].mean()
        quantity =df['category'].value_counts()
        result = pd.DataFrame({"avg_dist":avg_distance, "category_qty" : quantity})
        return result
    else:
        avg_distance = df.groupby('category')['distance'].mean()
        quantity =df['category'].value_counts()
        result = pd.DataFrame({"avg_dist":avg_distance, "category_qty" : quantity})
        #print(f"The following categories are missing: {', '.join(missing_categories)}")
        return result

def one_venue_avg_distance (df):
    
        avg_distance = df.groupby('category')['distance'].mean()
        quantity =df['category'].value_counts()
        result = pd.DataFrame({"avg_dist":avg_distance, "category_qty" : quantity})
        return result
    