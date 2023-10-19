class LoadUnload:
    """
    Simulate loading/unloading goods on/from truck
    ...
    Methods
    -----------------------------------------------
    load():
        control if weight of goods you want to load
        isn't too big for this car
    unload():
        control if weight of goods on your car
        is not less than you want to unload
    """
    def load(self, truck):
        self.truck = truck
        weight_ctr = self.truck.car_capacity
        while weight_ctr:
            print("\tThere's", self.truck.car_capacity - weight_ctr, "kg on car now. Full capacity:", self.truck.car_capacity)
            try:
                weight_in = int(input("Enter weight of goods to load in kg: "))
            except ValueError:
                print("\n\tInteger number (kg) expected\n")
            else:
                if weight_ctr - weight_in >= 0:
                    weight_ctr -= weight_in
                else:
                    print("\n\tIt's too heavy for this car\n")
        print("\n\tFully loaded:", self.truck.car_capacity - weight_ctr, "kg. Good drive!")
        return self.truck.car_capacity - weight_ctr

    def unload(self, load):
        print("\n\tUnloading...\n")
        while load > 0:
            print("\tThere's", load, "kg on car now")
            try:
                weight_out = int(input("Enter weight of goods to unload in kg: "))
            except ValueError:
                print("\n\tInteger number (kg) expected\n")
                print("\tThere's", load, "kg on car now")
            else:
                if weight_out <= load:
                    load -= weight_out
                else:
                    print("\n\tThere's not enough goods on your car\n")
        print("\n\tUnloading finished. See ya again!")
