import requests
import json
import pandas as pd
from getpass import getpass
import os
from dotenv import load_dotenv
load_dotenv()
from pymongo import MongoClient
client = MongoClient("localhost:27017")
db = client["ironhack"]
c = db.get_collection("companies")

def mongo_search (*cond):
    query = list(c.find({"$and": list(cond)}, projection= {"name":1,"category_code":1, "offices.city":1,'_id':0, "number_of_employees":1,'founded_year':1,
                                                           "total_money_raised":1, "offices.latitude":1, "offices.longitude":1}))
    df=pd.DataFrame(query)
    df['city1'] = df['offices'].apply(lambda x: x[0]['city'] if x and len(x) > 0 else None)
    df['city2'] = df['offices'].apply(lambda x: x[1]['city'] if x and len(x) > 1 else None)
    df['lat'] = [x[0]['latitude'] if x and 'latitude' in x[0] else 'N/A' for x in df['offices']]
    df['lon'] = [x[0]['longitude'] if x and 'longitude' in x[0] else 'N/A' for x in df['offices']]
    
    df.drop('offices', axis=1, inplace=True)
    df =df.sort_values('founded_year',ascending =False)
    
    return df


def requests_for_foursquare (query, lat, lon, radius=700, limit=2):

    url = f"https://api.foursquare.com/v3/places/search?query={query}&ll={lat}%2C{lon}&radius={radius}&limit={limit}"

    headers = {
        "accept": "application/json",
        "Authorization": token
    }
    
    try:
        f4_answer = requests.get(url, headers=headers).json()
    except:
        print("no :(")
    
    answer_list = []
    answer = f4_answer["results"]
    
    for element in answer:
        
        name = element["name"]
        address = element["location"]["address"]
        distance = element["distance"]
        lat = element["geocodes"]["main"]["latitude"]
        lon = element["geocodes"]["main"]["longitude"]
        
        small_dict = {
        "name": name,
        "address": address,
        "distance": distance,
        "lat": lat,
        "lon": lon}
        
        answer_list.append(small_dict)
        
    
    df=pd.DataFrame(answer_list)
    return df
