"""add banned field to user

Revision ID: 3b979de04914
Revises: e34d872812fe
Create Date: 2025-12-19 19:11:18.617195

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3b979de04914'
down_revision: Union[str, Sequence[str], None] = 'e34d872812fe'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
