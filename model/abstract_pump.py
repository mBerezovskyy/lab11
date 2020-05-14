from model.abstract_watering_tool import AbstractWateringTool
from abc import ABC


class AbstractPump(AbstractWateringTool, ABC):
    def __init__(self, price_in_uah=0, weight_in_gramms=0, country_where_created='', warranty_period_in_months=0,
                 body_material='', brand='', power_in_kilowatts=0, type_of_pumped_liquid=""):
        super().__init__(price_in_uah, weight_in_gramms,
                         country_where_created, warranty_period_in_months,
                         body_material,
                         brand)
        self.power_in_kilowatts = power_in_kilowatts
        self.type_of_pumped_liquid = type_of_pumped_liquid

    def __str__(self):
        return super().__str__() + \
                f"power_in_kilowatts : {self.power_in_kilowatts}, "\
                f"type_of_pumped_liquid: {self.type_of_pumped_liquid}"
