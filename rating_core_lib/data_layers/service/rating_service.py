from core_lib.data_layers.service.service import Service
from core_lib.data_transform.result_to_dict import ResultToDict
from rating_core_lib.data_layers.data_access.rating_data_access import RatingDataAccess


class RatingService(Service):

    def __init__(self, rating_da: RatingDataAccess):
        self._rating_da = rating_da

    @ResultToDict()
    def rate(self, user_id: int, target_id: int, target_type: int, rating_value: int = None):
        return self._rating_da.rate(user_id, target_id, target_type, rating_value)

    @ResultToDict()
    def all_user(self, user_id: int):
        return self._rating_da.all_by_user(user_id)
