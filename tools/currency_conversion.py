import os 
from utils.currency_converter import CurrencyConverter
from typing import List
from langchain.tools import tool
from dotenv import load_dotenv
load_dotenv()

class CurrencyConverterTool:
    def __init__(self):
        load_dotenv()
        self.api_key = os.environ.get("EXCHANGE_RATE_API_KEY") 
        self.currency_service = CurrencyConverter(self.api_key) # creating instance of class written in utils
        self.currency_converter_tool_list = self._setup_tools()

    def _setup_tools(self)-> List:
        """Setup all the tools for the currency converter tool"""
        @tool 
        def convert_currency(amount: float, from_currency: str,to_currency:str):
            """Convert the amount from one currency to another"""
            return self.currency_service.convert(amount,from_currency,to_currency)
        return [convert_currency]
    




