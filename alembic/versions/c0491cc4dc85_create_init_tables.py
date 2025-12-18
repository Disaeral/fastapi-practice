"""create init tables

Revision ID: c0491cc4dc85
Revises: 
Create Date: 2025-12-11 18:04:16.033601

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c0491cc4dc85'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    print("migration has started -> up")
    pass


def downgrade() -> None:
    """Downgrade schema."""
    print("migration has started -> down")
    pass
