import os
from utils.palce import GooglePlaceSearchTool, TavilyPlaceSearchTool
from typing import List
from langchain.tools import tool
from dotenv import load_dotenv

class PlaceSearchTool:
    def __init__(self):
        load_dotenv()
        self.google_api_key = os.environ.get("GPLACE_API_KEY")
        self.google_place_search = GooglePlaceSearchTool(self.google_api_key)
        self.tavily_search = TavilyPlaceSearchTool()
        self.place_search_tool_list = self._setup_tools()

    def _setup_tool(self) -> List:
        """Setup all the tools for the place search tool"""
        @tool 
        def search_attractions(place:str) -> str:
            """Search attractions of a place"""
            try: 
                attraction_result = self.google_place_search.google_search_attractions(place)
                if attraction_result:
                    return f"Following are the attraction after  google search results of {place} as suggested by google: {attraction_result}"
            except:
                tavily_result = self.tavily_search.tavily_search_attractions(place)
                if tavily_result: 
                    return f"Following are the attraction after  google search results of {place} as suggested by Tavily results: {tavily_result}"
                
        @tool
        def search_restaurants(place:str) -> str:
            """Search restaurants of a place"""
            try:
                restaurants_result = self.google_place_search.google_search_restaurants(place)
                if restaurants_result:
                    return f"Following are the restaurants of {place} as suggested by google: {restaurants_result}"
            except Exception as e:
                tavily_result = self.tavily_search.tavily_search_restaurants(place)
                return f"Google cannot find the details due to {e}. \nFollowing are the restaurants of {place}: {tavily_result}"  ## Fallback search using tavily in case google places fail
        
        @tool
        def search_activities(place:str) -> str:
            """Search activities of a place"""
            try:
                restaurants_result = self.google_place_search.google_search_activity(place)
                if restaurants_result:
                    return f"Following are the activities in and around {place} as suggested by google: {restaurants_result}"
            except Exception as e:
                tavily_result = self.tavily_search.tavily_search_activity(place)
                return f"Google cannot find the details due to {e}. \nFollowing are the activities of {place}: {tavily_result}"  ## Fallback search using tavily in case google places fail
        
        @tool
        def search_transportation(place:str) -> str:
            """Search transportation of a place"""
            try:
                restaurants_result = self.google_place_search.google_search_transportation(place)
                if restaurants_result:
                    return f"Following are the modes of transportation available in {place} as suggested by google: {restaurants_result}"
            except Exception as e:
                tavily_result = self.tavily_search.tavily_search_transportation(place)
                return f"Google cannot find the details due to {e}. \nFollowing are the modes of transportation available in {place}: {tavily_result}"  ## Fallback search using tavily in case google places fail
        
        return [search_attractions, search_restaurants, search_activities, search_transportation]
