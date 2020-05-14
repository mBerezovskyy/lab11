from model.abstract_pump import AbstractPump


class SubmersiblePump(AbstractPump):
    def __init__(self, power_in_kilowatts=0, type_of_pumped_liquid=0, productivity_in_litres_per_hour=0,
                 max_preasure_in_bars=0):
        super().__init__(power_in_kilowatts, type_of_pumped_liquid)
        self.productivity_in_litres_per_hour = productivity_in_litres_per_hour
        self.max_preasure_in_bars = max_preasure_in_bars

    def __str__(self):
        return super().__str__() + \
                f"productivity_in_litres_per_hour : {self.productivity_in_litres_per_hour}, "\
                f"max_preasure_in_bars: {self.max_preasure_in_bars}"
