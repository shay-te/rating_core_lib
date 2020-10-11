from core_lib.data_layers.service.service import Service
from rating_core_lib.data_layers.data_access.rating_data_access import RatingDataAccess


class RatingService(Service):

    def __init__(self, rating_da: RatingDataAccess):
        self._rating_da = rating_da

    def rate(self, user_id: int, target_id: int, target_type: int, rating_type: int, rating_value: int = None):
        self._rating_da.rate(user_id, target_id, target_type, rating_type, rating_value)
