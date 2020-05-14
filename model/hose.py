from model.abstract_watering_tool import AbstractWateringTool


class Hose(AbstractWateringTool):

    def __init__(self, price_in_uah=0, weight_in_gramms=0, country_where_created='', warranty_period_in_months=0,
                 body_material='', brand='', length_in_meters=0, thickness_in_milimetres=0, diameter_in_centimetres=0):
        super().__init__(price_in_uah, weight_in_gramms, country_where_created, warranty_period_in_months,
                         body_material, brand)
        self.length_in_meters = length_in_meters
        self.thickness_in_milimetres = thickness_in_milimetres
        self.diameter_in_centimetres = diameter_in_centimetres

    def __str__(self):
        return super().__str__() + \
            f"length_in_meters : {self.length_in_meters}, " \
            f"thickness_in_milimetres : {self.thickness_in_milimetres}, " \
            f"diameter_in_centimetres : {self.diameter_in_centimetres}"
