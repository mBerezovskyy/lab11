from typing import List
from model.hose import Hose


class WateringManager:

    def __init__(self, tools: List[Hose]):
        self.tools = tools

    def find_tools_greater_than(self, price):
        """
        >>> list_of_tools = [Hose(price_in_uah=20), Hose(price_in_uah=10), Hose(price_in_uah=5)]
        >>> watering_manager = WateringManager(list_of_tools)
        >>> found_tools_count = watering_manager.find_tools_greater_than(10)
        >>> found_tools_count
        1
        """
        found_tools = []
        for tool in self.tools:
            if tool.price_in_uah > price:
                found_tools.append(tool)
        return len(found_tools)

    def find_tools_by_warranty_period_in_months(self, period):
        """
        >>> list_of_tools = [Hose(warranty_period_in_months=2), Hose(warranty_period_in_months=4), \
        Hose(warranty_period_in_months=3)]
        >>> watering_manager = WateringManager(list_of_tools)
        >>> found_tools_count = watering_manager.find_tools_by_warranty_period_in_months(2)
        >>> found_tools_count
        1
        """
        found_tools = []
        for tool in self.tools:
            if tool.warranty_period_in_months == period:
                found_tools.append(tool)
        return len(found_tools)


if __name__ == "main":
    import doctest

    doctest.testmod(verbose=True)
