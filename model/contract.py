from flask.json import JSONEncoder


class BaseContract(JSONEncoder):
    def __init__(self, id=0):
        super().__init__()
        self.id = id


class GasStation(BaseContract):
    def __init__(self,
                 id=0,
                 latitude=0,
                 longitude=0,
                 franchise=False,
                 has_br_mania=False,
                 favorite=False):
        super().__init__(id)
        self.latitude = latitude
        self.longitude = longitude
        self.franchise = franchise
        self.has_br_mania = has_br_mania
        self.favorite = favorite


class Product(BaseContract):
    # {
    #     "id": 1,
    #     "name": "Hambúrguer",
    #     "price": 650,
    #     "category": "fast_food",
    #     "image": "https://www.zonasul.com.br/ImgProdutos/430_430/46069.jpg",
    #     "arrangement": "[0,6,8,9,10]",
    #     "premia_bonus": 300,
    #     "price_with_discount": 450
    # }
    def __init__(self, id=0, name=None, price=0, category=None, image=None, arrangement=None, premia_bonus=0,
                 price_with_discount=0):
        super().__init__(id)
        self.name = name
        self.price = price
        self.category = category
        self.image = image
        self.arrangement = arrangement
        self.premia_bonus = premia_bonus
        self.price_with_discount = price_with_discount
