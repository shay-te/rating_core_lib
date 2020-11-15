"""crate_db 

Revision ID: 1
Revises: 
Create Date: 2020-11-15 14:00:31.989109

"""
from datetime import datetime

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
from rating_core_lib.data_layers.data.db.entities.rating import Rating

revision = '1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        Rating.__tablename__,
        sa.Column(Rating.id.key, sa.Integer, primary_key=True, nullable=False),
        sa.Column(Rating.user_id.key, sa.Integer, nullable=False),
        sa.Column(Rating.target_id.key, sa.Integer, nullable=False),
        sa.Column(Rating.target_type.key, sa.Integer, nullable=False),
        sa.Column(Rating.rating_value.key, sa.Integer, nullable=False),

        sa.Column(Rating.created_at.key, sa.DateTime, default=datetime.utcnow),
        sa.Column(Rating.updated_at.key, sa.DateTime, default=datetime.utcnow),
        sa.Column(Rating.deleted_at.key, sa.DateTime, default=None),

        sa.Index(Rating.INDEX_USER_TO_TARGET, Rating.user_id.key, Rating.target_id.key, unique=False)
    )


def downgrade():
    op.drop_table(Rating.__tablename__)
