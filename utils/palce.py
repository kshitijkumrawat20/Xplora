import os 
import json 
from langchain_tavily import TavilySearch 
from langchain_google_community import GooglePlacesTool, GooglePlacesAPIWrapper
from langchain_tavily import TavilySearch
from serpapi import GoogleSearch
from typing import Dict, List, Union
class GooglePlaceSearchTool:
    def __init__(self, api_key: str):
        self.places_wrapper = GooglePlacesAPIWrapper(gplaces_api_key = api_key)
        self.places_tool = GooglePlacesTool(api_wrapper = self.places_wrapper)
        
    def google_search_attractions(self, place: str) -> dict:
        """
        searcher for attraction of places in the specified place using GooglePlaces API.
        """
        return self.places_tool.run(f"top attractive places in and around {place}")
    
    def google_search_restaurants(self, place:str) -> dict:
        """
        Searches for available restaurants in the specified place using GooglPlaceAPI
        """
        return self.places_tool.run(f"what are the top 10 restaurants and eateries in and around {place}?")
    
    def google_search_activity(self, place:str) -> dict:
        """
        Searches for popular activities in the specified place using GooglePlaces API.       
        """
        return self.places_tool(f"Activities in and around {[place]}")
    
    def google_search_transportation(self, place: str) -> dict:
        """
        Searches for available modes of transportation in the specified place using GooglePlaces API.
        """
        return self.places_tool.run(f"What are the different modes of transportations available in {place}")

class TavilyPlaceSearchTool:
    def __init__(self, api_key: str):
        self.tavily_tool = TavilySearch(topic = "general", include_answer = "advanced", api_key = api_key)

    def tavily_search_attractions(self, place: str) -> dict:
        """
        searcher for attraction of places in the specified place using TavilySearch API.
        """
        result = self.tavily_tool.invoke({"query":f"top attractive places in and around {place}"})
        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]
        return result

    def tavily_search_restaurants(self, place:str) -> dict:
        """
        Searches for available restaurants in the specified place using TavilySearch API
        """
        result = self.tavily_tool.invoke({"query": f"what are the top 10 restaurants and eateries in and around {place}."})
        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]
        return result
    
    def tavily_search_activity(self, place:str) -> dict:
        """
        Searches for popular activities in the specified place using TavilySearch  API.       
        """
        result = self.tavily_tool.invoke({"query": f"activities in and around {place}"})
        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]
        return result
    
    def tavily_search_transportation(self, place: str) -> dict:
        """
        Searches for available modes of transportation in the specified place using TavilySearch API.
        """
        result = self.tavily_tool.invoke({"query": f"What are the different modes of transportations available in {place}"})
        if isinstance(result, dict) and result.get("answer"):
            return result["answer"]
        return result

class SerpapiPlaceSearchTool:
    def __init__(self):
        self.api_key = os.getenv("SERPAPI_KEY")
        self.key_to_remove = [
            'place_id', 'data_id', 'data_cid', 'reviews_link', 'photos_link',
            'gps_coordinates', 'place_id_search', 'provider_id', 'type_id',
            'type_ids', 'open_state', 'operating_hours', 'extensions',
            'service_options', 'thumbnail', 'serpapi_thumbnail'
        ]
    
    def _clean_results(self, results:list) -> list:
        """Remove unwanted keys from each result dict."""
        for item in results:
            for key in self.key_to_remove:
                item.pop(key,None)
        return results

    def Serpapi_search_attractions(self, place: str) -> Union[List[Dict], Dict]:
        """
        searcher for attraction of places in the specified place using SerpAPI.
        """
        params = {
            "api_key": self.api_key,
            "engine": "google_maps",
            "q": f"places of attraction in {place}",
            "google_domain": "google.com",
            "type": "search",
            "hl": "en"
            }
        
        search = GoogleSearch(params)
        result = search.get_dict()
        if isinstance(result, dict) and result.get("local_results"):
            cleaned = self._clean_results(result["local_results"])
            cleaned.sort(key=lambda x: x.get("reviews_count", 0), reverse=True)
            return cleaned[:10]
        return result[:10]

    def Serpapi_search_restaurants(self, place:str) -> dict:
        """
        searcher for restaurants and hotels of specified place using SerpAPI.
        """
        params = {
            "api_key": self.api_key,
            "engine": "google_maps",
            "q": f"restaurants and hotels in {place}",
            "google_domain": "google.com",
            "type": "search",
            "hl": "en"
            }
        
        search = GoogleSearch(params)
        result = search.get_dict()
        if isinstance(result, dict) and result.get("local_results"):
            cleaned = self._clean_results(result["local_results"])
            cleaned.sort(key=lambda x: x.get("reviews_count", 0), reverse=True)
            return cleaned[:5]
        return result[:5]
    
    def Serpapi_search_activity(self, place:str) -> dict:
        """
        Searches for popular activities in the specified place using TavilySearch  API.       
        """
        params = {
            "api_key": self.api_key,
            "engine": "google_maps",
            "q": f"popular activities in {place}",
            "google_domain": "google.com",
            "type": "search",
            "hl": "en"
            }
        search = GoogleSearch(params)
        result = search.get_dict()
        if isinstance(result, dict) and result.get("local_results"):
            cleaned = self._clean_results(result["local_results"])
            cleaned.sort(key=lambda x: x.get("reviews_count", 0), reverse=True)
            return cleaned[:5]
        return result[:5]
    
    # def Serpapi_search_transportation(self, place: str) -> dict:
    #     """
    #     Searches for available modes of transportation in the specified place using TavilySearch API.
    #     """
    #     result = self.tavily_tool.invoke({"query": f"What are the different modes of transportations available in {place}"})
    #     if isinstance(result, dict) and result.get("answer"):
    #         return result["answer"]
    #     return result