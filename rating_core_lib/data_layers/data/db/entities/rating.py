from sqlalchemy import Integer, Column, Index

from core_lib.data_layers.data.db.sqlalchemy.base import Base
from core_lib.data_layers.data.db.sqlalchemy.mixins.time_stamp_mixin import TimeStampMixin


class Rating(Base, TimeStampMixin):

    __tablename__ = 'rating'

    INDEX_USER_TO_TARGET = 'user_to_target'

    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, nullable=False)
    target_id = Column(Integer, nullable=False)
    target_type = Column(Integer, nullable=False)
    rating_value = Column(Integer)

    __table_args__ = (Index(INDEX_USER_TO_TARGET, 'user_id', 'target_id', unique=False),)
