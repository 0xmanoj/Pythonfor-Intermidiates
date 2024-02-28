#Importing Modules 
import requests 
import json 
from datetime import datetime 
import time

#API Endpoints 
url_soil_fertility = 'https://api.agromonitoring.com/agro/1.0/soil?appid=<Your_App_ID>'
url_soil_humidity = 'https://api.agromonitoring.com/agro/1.0/soil/humidity?appid=<Your_App_ID>'
url_soil_temperature = 'https://api.agromonitoring.com/agro/1.0/soil/temperature?appid=<Your_App_ID>'

#Data points 
data_points = {
    'wind': '', 
    'light': '', 
    'water': '', 
    'food': '', 
    'ph': '',
    'crop_growth': '', 
    'expected_yield': ''
}

#Function to get Soil Fertility Data 
def get_soil_fertility():
    response = requests.get(url_soil_fertility) 
    response_json = response.json() 
    data_points['soil_fertility'] = response_json['soil_fertility']

#Function to get Soil Humidity Data 
def get_soil_humidity():
    response = requests.get(url_soil_humidity) 
    response_json = response.json() 
    data_points['soil_humidity'] = response_json['soil_humidity']

#Function to get Soil Temperature Data 
def get_soil_temperature():
    response = requests.get(url_soil_temperature) 
    response_json = response.json() 
    data_points['soil_temperature'] = response_json['soil_temperature']

#Function to Post Data to Cloud and IOT 
def post_data_to_cloud_iot():
    data_points['timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data_points_json = json.dumps(data_points)
    requests.post('https://api.agromonitoring.com/agro/1.0/cloud', data=data_points_json)

#Main Function - Executes all the functions 
def main():
    while True:
        get_soil_fertility()
        get_soil_humidity()
        get_soil_temperature()
        post_data_to_cloud_iot()
        time.sleep(5)

#Executing the main function 
if _name_ == '_main_':
    main()