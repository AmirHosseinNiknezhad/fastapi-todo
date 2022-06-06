"""add users table

Revision ID: ac7afc758b59
Revises: 73bf1156414b
Create Date: 2022-05-24 18:50:26.895065

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "ac7afc758b59"
down_revision = "73bf1156414b"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column("email", sa.String, unique=True, nullable=False, index=True),
        sa.Column("username", sa.String, unique=True, nullable=False, index=True),
        sa.Column("password", sa.String, nullable=False),
        sa.Column("active", sa.Boolean, server_default="true"),
        sa.Column(
            "created", sa.TIMESTAMP(timezone=True), server_default=sa.text("now()")
        ),
    )


def downgrade():
    op.drop_table("users")
