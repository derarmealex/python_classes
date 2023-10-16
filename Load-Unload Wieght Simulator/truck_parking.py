class TruckParking:
    """
    Truck parking
    ...
    Methods
    ---------------------------------------------------
    __init__():
        retrieves truck model with data of its capacity
    truck_info():
        returns capacity of truck
    go_load():
        sends truck to loading
    """
    __slots__ = ["model", "car_capacity"]

    def __init__(self, model, car_capacity):
        self.model = model
        self.car_capacity = car_capacity

    def truck_info(self):
        return self.car_capacity

    def go_load(self, load_unload):
        load_unload.load(self)
