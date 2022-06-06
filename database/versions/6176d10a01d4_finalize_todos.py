"""finalize todos

Revision ID: 6176d10a01d4
Revises: ac7afc758b59
Create Date: 2022-05-24 20:20:12.502709

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "6176d10a01d4"
down_revision = "ac7afc758b59"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("todos", sa.Column("done", sa.Boolean, server_default="false"))
    op.add_column(
        "todos",
        sa.Column(
            "created", sa.TIMESTAMP(timezone=True), server_default=sa.text("now()")
        ),
    )
    op.add_column(
        "todos",
        sa.Column(
            "owner_id", sa.Integer, sa.ForeignKey("users.id", ondelete="CASCADE")
        ),
    )


def downgrade():
    op.drop_column("todos", "done")
    op.drop_column("todos", "created")
    op.drop_column("todos", "owner_id")
