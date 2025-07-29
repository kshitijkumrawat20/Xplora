import os 
import json 
from langchain_tavily import TavilySearch 
from langchain_google_community import GooglePlaceTool, GooglePlacesAPIWrapper

class GooglePlaceSearchTool:
    def __init__(self, api_key: str):
        self.places_wrapper = GooglePlaceAPIWrapper(gplaces_api_key = api_key)
        self.places_tool = GooglePlaceTool(api_wrapper = self.places_wrapper)

    def google_search_attractions(self, place: str) -> dict:
        """
        searcher for attraction of places in the specified place using GooglePlaces API.
        """
        return self.places_tool.(f"What are the top 10 restaurants and easteries in and around {places}")