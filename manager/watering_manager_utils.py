from model.sorting_type import SortingType
from typing import List
from model.hose import Hose


class WateringManagerUtils:

    def __init__(self, tools: List[Hose]):
        self.tools = tools

    def sort_tools_by_price(self, sorting_type: SortingType):
        """
        >>> list_of_tools = [Hose(price_in_uah=20), Hose(price_in_uah=10), Hose(price_in_uah=5)]
        >>> watering_manager_utils = WateringManagerUtils(list_of_tools)
        >>> sorted_tools_asc = watering_manager_utils.sort_tools_by_price(SortingType.ASC)
        >>> [tool.price_in_uah for tool in sorted_tools_asc]
        [5, 10, 20]
        >>> sorted_tools_desc = watering_manager_utils.sort_tools_by_price(SortingType.DESC)
        >>> [tool.price_in_uah for tool in sorted_tools_desc]
        [20, 10, 5]
        """
        if sorting_type == SortingType.ASC:
            return sorted(self.tools, key=lambda tool: tool.price_in_uah)
        elif sorting_type == SortingType.DESC:
            return sorted(self.tools, key=lambda tool: tool.price_in_uah, reverse=True)


if __name__ == "main":
    import doctest

    doctest.testmod(verbose=True)
