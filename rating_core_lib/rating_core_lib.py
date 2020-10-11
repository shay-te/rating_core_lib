from core_lib.data_layers.data.handler.sql_alchemy_data_handler_factory import SqlAlchemyDataHandlerFactory
from omegaconf import DictConfig
from core_lib.core_lib import CoreLib


class RatingCoreLib(CoreLib):

    def __init__(self, conf: DictConfig):
        self.config = conf      

        db_data_session = SqlAlchemyDataHandlerFactory(self._config.core_lib.data.sqlalchemy)
