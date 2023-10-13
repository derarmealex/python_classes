class TruckParking:
    """
    Truck parking
    ...
    Methods
    --------------------------------------------------
    __init__():
        retrieve truck model with data of its capacity
    truck_info():
        return capacity of truck
    go_load():
        send truck to loading
    """
    model = None
    car_capacity = 0

    def __init__(self, model, car_capacity):
        self.model = model
        self.car_capacity = car_capacity

    def truck_info(self):
        return self.car_capacity

    def go_load(self, load_unload):
        load_unload.load(self)
