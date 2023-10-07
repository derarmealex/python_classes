class LoadUnload:
    """
    Simulate loading/unloading goods
    ...
    Methods
    -----------------------------------------------
    load(car_capacity):
        Control if weight of goods you want to load
        isn't too big for this car
    unload(load):
        Control if weight of goods on your car
        is not less than you want to unload
    """
    def __init__(self):
        """
        set attributes for LoadUnload
        ...
        Attributes
        ----------
        """
    def load(self, car_capacity):
        while True:
            try:
                weight_in = int(input("Enter weight of goods to load in kg: "))
            except ValueError:
                print("\n\tInteger number (kg) expected\n")
            else:
                if weight_in <= car_capacity:
                    return int(weight_in)
                else:
                    print("\n\tIt's too heavy for this car\n")

    def unload(self, load):
        while load > 0:
            try:
                weight_out = int(input("Enter weight of goods to unload in kg: "))
            except ValueError:
                print("\n\tInteger number (kg) expected\n")
                print("\tThere's", load, "kg on car now")
            else:
                if weight_out <= load:
                    load = load - weight_out
                else:
                    print("\n\tThere's not enough goods on your car\n")
                print("\tThere's", load, "kg on car now")
        print("\n\tUnloading finished. See ya again!")
