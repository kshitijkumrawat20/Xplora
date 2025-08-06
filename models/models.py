from pydantic import BaseModel, Field
from typing import List


class HotelCostInput(BaseModel):
    price_per_night: float = Field(..., description="Price per night in local currency")
    total_day: float = Field(..., description="Number of nights")

class CostsInput(BaseModel):
    costs: List[float]

class DailyExpensesCalculation(BaseModel):
    total_cost : float= Field(..., description="Total expense of trip")
    days : int = Field(...,description="Number of days of trip")