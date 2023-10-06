class LoadUnload:
    """
    Simulate loading / unloading goods
    ...
    Methods
    ------------------------------------------------
    load(car_capacity):
        Control if weight of goods you want to load
        isn't too much for this car

    unload(load):
        Control if you have enough goods on your car
        that you want to unload
    """
    def load(self, car_capacity):
        while True:
            try:
                weight_in = int(input("Enter weight of goods to load: "))
            except ValueError:
                print("\n\tIncorrect number! Try again\n")
            else:
                if weight_in <= car_capacity:
                    return int(weight_in)
                else:
                    print("\n\tit's too heavy!\n")

    def unload(self, load):
        while load > 0:
            try:
                weight_out = int(input("Enter weight of goods to unload: "))
            except ValueError:
                print("\n\tIncorrect number! Try again\n")
                print("\tThere's", load, "kg on car now")
            else:
                if weight_out <= load:
                    load = load - weight_out
                else:
                    print("\n\tIt's not enough goods on your car!\n")
                print("\tThere's", load, "kg on car now")
        print("\n\tUnloading finished. See ya again!")
