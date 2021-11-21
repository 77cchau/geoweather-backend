import json
import urllib.parse
import urllib.request

import mapping

WEATHER_URL_BASE = "https://api.weather.gov/points/"



def build_weather_url(lat,lon):
    return f"{WEATHER_URL_BASE}{lat},{lon}"

'''
Uses link to give back the forecast data for a location
    Uses a URL to give back the dataset associated with a particular location based on 
    API data
'''
def build_weather_data(url):
    response = None
    try:
        request = urllib.request.Request(url)
        response = urllib.request.urlopen(request)
        #Get a JSON response
        json_text = response.read().decode(encoding = "utf-8")

        return json.loads(json_text)
    finally:
        #close
        if response != None:
            response.close()

'''
Uses data of a location to return a forecast API link
    The forecast for a location in the API is in and of itself another link in the API, so we have
    to load this url to get the forecast data
'''
def build_forecast_data(lat, lon):
    url = build_weather_url(lat,lon)
    data = build_weather_data(url)

    forecast_url = data["properties"]["forecast"]

    response = None
    try:
        request = urllib.request.Request(forecast_url)
        response = urllib.request.urlopen(request)
        #Get a JSON response
        json_text = response.read().decode(encoding = "utf-8")

        return json.loads(json_text)
    finally:
        #close
        if response != None:
            response.close()

'''
Returns a TUPLE of the most current and the next forecast of the day (in the API, this is
the 0th and 1st index of an array called associated with the "periods" key in "properties")
    Uses "Detailed Forecast" on the pro

def get_todays_forecast(city,state):
    (lat,lon) = mapping.get_coords(city,state)
    return (build_forecast_data(lat,lon)["properties"]["periods"][0]["detailedForecast"],
            build_forecast_data(lat,lon)["properties"]["periods"][1]["detailedForecast"])
'''

def get_forecast_data(city,state):
    (lat,lon) = mapping.get_coords(city,state)
    return build_forecast_data(lat,lon)["properties"]["periods"]