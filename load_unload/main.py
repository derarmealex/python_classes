import load_unload
help(load_unload)

truck = load_unload.LoadUnload()

car_capacity = 3000
truck.unload(truck.load(car_capacity))
