"""added user model and relationships

Revision ID: 337ddd64a407
Revises: 
Create Date: 2021-12-18 16:45:11.821266

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "337ddd64a407"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("email", sa.String(), nullable=True),
        sa.Column("password", sa.String(), nullable=True),
        sa.Column("joined", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_users_id"), "users", ["id"], unique=False)
    op.create_table(
        "posts",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("added", sa.DateTime(), nullable=True),
        sa.Column("body", sa.String(), nullable=True),
        sa.Column("user_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_posts_body"), "posts", ["body"], unique=False)
    op.create_index(op.f("ix_posts_id"), "posts", ["id"], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_posts_id"), table_name="posts")
    op.drop_index(op.f("ix_posts_body"), table_name="posts")
    op.drop_table("posts")
    op.drop_index(op.f("ix_users_id"), table_name="users")
    op.drop_table("users")
    # ### end Alembic commands ###
