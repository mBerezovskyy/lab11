from abc import ABC


class AbstractWateringTool(ABC):

    def __init__(self, price_in_uah=0, weight_in_gramms=0, country_where_created='', warranty_period_in_months=0,
                 body_material='', brand=''):
        self.price_in_uah = price_in_uah
        self.weight_in_gramms = weight_in_gramms
        self.country_where_created = country_where_created
        self.warranty_period_in_months = warranty_period_in_months
        self.body_material = body_material
        self.brand = brand

    def __str__(self):
        return \
            f"price_in_uah: {self.price_in_uah}, " \
            f"weight_in_gramms: {self.weight_in_gramms}, " \
            f"country_where_created: {self.country_where_created}, " \
            f"warranty_period_in_months: {self.warranty_period_in_months}, " \
            f"body_material: {self.body_material}"
