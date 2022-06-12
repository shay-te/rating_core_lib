import inspect
import os

from core_lib.alembic.alembic import Alembic
from core_lib.connection.sql_alchemy_connection_registry import SqlAlchemyConnectionRegistry
from omegaconf import DictConfig
from core_lib.core_lib import CoreLib
from rating_core_lib.data_layers.data_access.rating_data_access import RatingDataAccess
from rating_core_lib.data_layers.service.rating_service import RatingService


class RatingCoreLib(CoreLib):

    def __init__(self, conf: DictConfig):
        CoreLib.__init__(self)
        self.config = conf      

        db_data_session = SqlAlchemyConnectionRegistry(self.config.core_lib.data.sqlalchemy)
        self.rating = RatingService(RatingDataAccess(db_data_session))

    @staticmethod
    def install(cfg: DictConfig):
        Alembic(os.path.dirname(inspect.getfile(RatingCoreLib)), cfg).upgrade()

    @staticmethod
    def uninstall(cfg: DictConfig):
        Alembic(os.path.dirname(inspect.getfile(RatingCoreLib)), cfg).downgrade()
