from sqlalchemy import Integer, Column, Index

from core_lib.data_layers.data.db.sqlalchemy.base import Base


class Rating(Base):
    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, nullable=False)
    target_id = Column(Integer, nullable=False)
    target_type = Column(Integer, nullable=False)
    rating_type = Column(Integer, nullable=False)
    rating_value = Column(Integer)

    __table_args__ = (Index('user_target_type', 'user_id', 'target_id', 'target_type', unique=True),)
