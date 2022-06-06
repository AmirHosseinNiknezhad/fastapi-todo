"""add cols to todos

Revision ID: 73bf1156414b
Revises: 86ca9cb6dbd8
Create Date: 2022-05-24 17:24:44.308481

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "73bf1156414b"
down_revision = "86ca9cb6dbd8"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("todos", sa.Column("importance", sa.Integer, server_default="1"))


def downgrade():
    op.drop_column("todos", "importance")
