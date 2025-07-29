import os 
from dotenv import load_dotenv
from langchain.tools import tool
from langchain_community.utilities.alpha_vantage import AlphaVantageAPIWrappers
load_dotenv()


@tool
def multily(a:int, b: int) -> int: 
    """
    Multily two integers.
    Args:
        a(int): The first integer 
        b(int): The second integer 

    Returns:
        int: The product of a and b 

    """
    return a*b 


@tool
def add(a:int, b: int) -> int: 
    """
    Multily two integers.
    Args:
        a(int): The first integer 
        b(int): The second integer 

    Returns:
        int: The product of a and b 

    """
    return a+b 




@tool
def currency_converter(from_curr: str, to_curr: str, value: float)->float:
    os.environ["ALPHAVANTAGE_API_KEY"] = os.getenv('ALPHAVANTAGE_API_KEY')
    alpha_vantage = AlphaVantageAPIWrapper()
    response = alpha_vantage._get_exchange_rate(from_curr, to_curr)
    print(response)
    exchange_rate = response['Realtime Currency Exchange Rate']['5. Exchange Rate']
    return value * float(exchange_rate)