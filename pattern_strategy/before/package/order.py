class Order():
    def __init__(self, shipper):
        self._shipper = shipper #This is bad, Order needs to know about shipper

    @property
    def shipper(self):
        return self._shipper

