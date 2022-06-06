"""create todos

Revision ID: 86ca9cb6dbd8
Revises: 
Create Date: 2022-05-24 17:05:25.522618

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "86ca9cb6dbd8"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "todos",
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column("title", sa.String, index=True, nullable=False),
        sa.Column("description", sa.String, index=True),
    )


def downgrade():
    op.drop_table("todos")
