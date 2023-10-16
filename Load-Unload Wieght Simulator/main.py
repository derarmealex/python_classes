import truck_parking
import load_unload
#help(truck)
#help(load_unload)

load_unload = load_unload.LoadUnload()
tatra = truck_parking.TruckParking("Tatra", 3000)

load_tatra = load_unload.load(tatra)
unload_tatra = load_unload.unload(load_tatra)
