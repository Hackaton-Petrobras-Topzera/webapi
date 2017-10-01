from model.contract import GasStation
from service.database import ProductDao, LocationDao


class GasStationService:
    def select_all_gas(self):
        return LocationDao().get_all_gas_stations_from_rj()


class ProductService:
    def search_only_arrangement(self, id):
        return ProductDao().get_only_arrangement(id)

    def select_all(self):
        return ProductDao().all()

    def find_by_id(self, id):
        return ProductDao().get_by_id(id)
