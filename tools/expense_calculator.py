from utils.expenses_calculator import calculator
from typing import List
from langchain.tools import tool

class CalculatorTool:
    def __init__(self):
        self.calculator = calculator()
        self.calculator_tool_list = self._setup_tool()

    def _setup_tool(self) -> List:
        """Setup all the tool for calculating expenses"""
        @tool 
        def estimate_total_hotel_cost(price_per_night:str, total_day:float) -> float:
            """calculate total hotel cost"""
            return self.calculator.multiply(price_per_night, total_day)
        @tool
        def calculate_total_expense(*costs: float) -> float:
            """Calculate total expense of the trip"""
            return self.calculator.calculate_total(*costs)
        
        @tool
        def calculate_daily_expense_budget(total_cost: float, days: int) -> float:
            """Calculate daily expense"""
            return self.calculator.calculate_daily_budget(total_cost, days)
        
        return [estimate_total_hotel_cost, calculate_total_expense, calculate_daily_expense_budget]
        

