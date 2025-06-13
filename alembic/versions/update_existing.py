"""update existing

Revision ID: update_existing
Revises: 5770332d85fc
Create Date: 2024-03-19 10:00:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'update_existing'
down_revision: Union[str, None] = '5770332d85fc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # No hacemos nada porque las tablas ya existen
    pass


def downgrade() -> None:
    # No hacemos nada porque no queremos eliminar las tablas
    pass 