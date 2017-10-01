from model.contract import GasStation


class GasStationService:
    def select_all_gas(self):
        gas = GasStation(id=1, latitude=-22.929741, longitude=-43.179529)
        gas2 = GasStation(id=2, latitude=-22.929692, longitude=-43.177769, favorite=True)
        gas3 = GasStation(id=3, latitude=-22.928299, longitude=-43.179496, franchise=True)

        all_gas = [gas, gas2, gas3]
        return all_gas
