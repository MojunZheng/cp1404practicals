from taxi import Taxi

class SilverServiceTaxi(Taxi):
    """Created a SilverServiceTaxi class"""
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness
