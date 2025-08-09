import requests
from datetime import date, timedelta
class WeatherForecast:
    # def __init__(self,api_key:str):
    def __init__(self):
        # self.api_key= api_key
        self.base_url = "https://api.openweathermap.org/data/2.5"
        self.base_url_ = "https://nominatim.openstreetmap.org/search"
    
    def get_coordinates(self,city_name:str):
        geo_url = self.base_url_
        params = {"q": city_name, "format": "json", "limit": 1}
        response = requests.get(geo_url, params=params, headers={"User-Agent": "weather-app"})
        response.raise_for_status()
        data = response.json()
        if not data:
            raise ValueError("City not found")
        return float(data[0]["lat"]), float(data[0]["lon"])

    def get_forecast_weather(self,place, days=5):
        lat, lon = self.get_coordinates(place)        
        start = date.today()
        end = start + timedelta(days=days-1)  # Open-Meteo includes both start & end
        
        weather_url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": lat,
            "longitude": lon,
            "daily": ["temperature_2m_max", "temperature_2m_min", "precipitation_sum"],
            "timezone": "auto",
            "start_date": start.isoformat(),
            "end_date": end.isoformat()
        }
        response = requests.get(weather_url, params=params)
        response.raise_for_status()
        return response.json()["daily"]
    
    def get_current_weather(self,place):
        """Get the current weather of the place"""
        lat, lon = self.get_coordinates(place)
        weather_url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": lat,
            "longitude": lon,
            "current_weather": True
        }
        response = requests.get(weather_url, params=params)
        response.raise_for_status()
        weather_data = response.json().get("current_weather", {})
        
        return {
            "city": place,
            "temperature": weather_data.get("temperature"),
            "windspeed": weather_data.get("windspeed"),
            "time": weather_data.get("time")
        }

    # def get_current_weather(self, place:str):
    #     """Get the current weather of the place"""
    #     try: 
    #         url = f"{self.base_url}/weather"
    #         params = {
    #             "q":place,
    #             "appid":self.api_key,
    #         }
    #         response = requests.get(url, params = params)
    #         return response.json() if response.status_code == 200 else {}
    #     except Exception as e:
    #         raise e
            
    # def get_forecast_weather(self, place:str):
    #     """Get weather forecast of a place"""
    #     try:
    #         url = f"{self.base_url}/forecast"
    #         params = {
    #             "q": place,
    #             "appid": self.api_key,
    #             "cnt": 10,
    #             "units": "metric"
    #         }
    #         response = requests.get(url, params=params)
    #         return response.json() if response.status_code == 200 else {}
    #     except Exception as e:
    #         raise 