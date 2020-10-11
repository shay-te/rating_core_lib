from core_lib.data_layers.data.handler.sql_alchemy_data_handler_factory import SqlAlchemyDataHandlerFactory
from core_lib.data_layers.data_access.data_access import DataAccess
from rating_core_lib.data_layers.data.db.entities.rating import Rating


class RatingDataAccess(DataAccess):

    def __init__(self, db: SqlAlchemyDataHandlerFactory):
        self.db = db

    def rate(self, user_id: int, target_id: int, target_type: int, rating_type: int, rating_value: int = None):
        existing_rating = self.get(user_id, target_id, target_type)

        with self.db.get() as session:
            if existing_rating:
                session.query(Rating)\
                        .filter(Rating.user_id == user_id,
                                Rating.target_id == target_id,
                                Rating.target_type == target_type)\
                        .update({Rating.rating_type: rating_type, Rating.rating_value: rating_value})
            else:
                rating = Rating()
                rating.user_id = user_id
                rating.target_id = target_id
                rating.target_type = target_type
                rating.rating_type = rating_type
                rating.rating_value = rating_value
                session.add(rating)

    def get(self, user_id: int, target_id: int, target_type: int):
        with self.db.get() as session:
            return session.query(Rating).filter(Rating.user_id == user_id, Rating.target_id == target_id, Rating.target_type == target_type).first()

