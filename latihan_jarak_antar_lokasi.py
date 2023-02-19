import pandas as pd
import googlemaps


data = pd.read_excel(r'data_uji_coba_jarak_antar_lokasi.xlsx','Sheet1')

API_key = 'AIzaSyDR-sUdAMhowQX6IxK91wb5QzYXxmuvaJ8'   #enter the key you got from Google. I removed mine here

gmaps = googlemaps.Client(key=API_key)



origin = (-2.01234699405899,29.377851313693) #Let's say this is the origin
destinations = data.coordinates


actual_duration = []


for destination in destinations:
    result = gmaps.distance_matrix(origin, destination, mode='driving')["rows"][0]["elements"][0]["duration"]["value"]  
    result = result/3600
    actual_duration.append(result)
    


#Add the list of coordinates to the main data set

data["duration (Hours)"] = actual_duration

actual_distance = []


for destination in destinations:
    result = gmaps.distance_matrix(origin, destination, mode='driving')["rows"][0]["elements"][0]["distance"]["value"]  
    result = result/1000
    actual_distance.append(result)
    


#Add the list of coordinates to the main data set

data["distance (Km)"] = actual_distance

data.to_excel('hasil_uji_coba_3.xlsx')