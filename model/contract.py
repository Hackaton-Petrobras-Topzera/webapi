from flask.json import JSONEncoder


class BaseContract(JSONEncoder):
    def __init__(self, id=0):
        super().__init__()
        self.id = id


class GasStation(BaseContract):
    def __init__(self,
                 latitude=0,
                 longitude=0,
                 franchise=False,
                 has_br_mania=False,
                 favorite=False):
        super().__init__()
        self.latitude = latitude
        self.longitude = longitude
        self.franchise = franchise
        self.has_br_mania = has_br_mania
        self.favorite = favorite
