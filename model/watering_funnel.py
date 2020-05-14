from model.abstract_watering_tool import AbstractWateringTool


class WateringFunnel(AbstractWateringTool):
    def __init__(self, price_in_uah=0, weight_in_gramms=0, country_where_created='', warranty_period_in_months=0,
                 body_material='', brand='', vollumeInLitres=0):
        super().__init__(price_in_uah, weight_in_gramms, country_where_created, warranty_period_in_months,
                         body_material, brand)
        self.vollumeInLitres = vollumeInLitres

    def __str__(self):
        return super().__str__() + \
                f"vollumeInLitres : {self.vollumeInLitres}, "