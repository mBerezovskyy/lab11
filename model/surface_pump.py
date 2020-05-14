from model.abstract_pump import AbstractPump


class SurfacePump(AbstractPump):
    def __init__(self, power_in_kilowatts=0, type_of_pumped_liquid=0, suctionTypeName=''):
        super().__init__(power_in_kilowatts, type_of_pumped_liquid)
        self.suctionTypeName = suctionTypeName

    def __str__(self):
        return super().__str__() + \
               f"suctionTypeName : {self.suctionTypeName}, "