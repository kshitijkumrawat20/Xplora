from typing import List
class calculator:
    @staticmethod
    def multiply(a:float, b: float) -> float:
        """
        Multiply two integers.
        Args:
            a (int): The first integer 
            b (int): The second integer

        Returns:
            int: The product of a and b 
        """ 
        return a * b 

    @staticmethod
    def calculate_total(costs: List[float]) -> float:
        """
        Calculate sum of the given list of numbers

        Args:
            x (list): List of floating numbers

        Returns:
            float: The sum of numbers in the list x
        """
        return sum(costs)

    @staticmethod
    def calculate_daily_budget(total:float,days: int) -> float:
        """
        Calculate daily budget

        Args:
            total (float): Total cost.
            days (int): Total number of days

        Returns:
            float: Expense for a single day
        """
        return total / days if days > 0 else 0

    