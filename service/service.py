from model.contract import Payment
from service.database import ProductDao, LocationDao, OrderDao, PaymentDao


class GasStationService:
    def select_all_gas(self):
        return LocationDao().get_all_gas_stations_from_rj()


class ProductService:
    def search_only_arrangement(self, id):
        return ProductDao().get_only_arrangement(id)

    def suggestions(self):
        return ProductDao().suggestions()

    def select_all(self):
        return ProductDao().all()

    def find_by_id(self, id):
        return ProductDao().get_by_id(id)


class OrderService:
    def select_opened_orders(self):
        return OrderDao().search_orders()

    def order_product(self):
        return OrderDao.post_order()


class PaymentService:
    def authorize(self, data):
        payment = Payment(number=data['number'], holder_name=data['holder_name'],
                          exp_month=data['exp_month'], exp_year=data['exp_year'],
                          cvv=data['cvv'], purchase=data['purchase'])
        return PaymentDao().save(payment), payment.id
