from utils.expenses_calculator import calculator
from typing import List
from langchain.tools import tool
from models.models import HotelCostInput,CostsInput,DailyExpensesCalculation
class CalculatorTool:
    def __init__(self):
        self.calculator = calculator()
        self.calculator_tool_list = self._setup_tool()

    def _setup_tool(self) -> List:
        """Setup all the tool for calculating expenses"""
        @tool (args_schema=HotelCostInput)
        def estimate_total_hotel_cost(price_per_night:float, total_day:float) -> float:
            """calculate total hotel cost"""
            # return self.calculator.multiply(price_per_night, total_day)
            return self.calculator.multiply(price_per_night, total_day)
        @tool(args_schema=CostsInput)
        def calculate_total_expense(costs: List[float]) -> float:
            """Calculate total expense of the trip"""
            return self.calculator.calculate_total(costs)
            # return sum(*costs)
        
        @tool(args_schema=DailyExpensesCalculation)
        def calculate_daily_expense_budget(total_cost: float, days: int) -> float:
            """Calculate daily expense"""
            return self.calculator.calculate_daily_budget(total_cost, days)
        
        return [estimate_total_hotel_cost, calculate_total_expense, calculate_daily_expense_budget]
        

