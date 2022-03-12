"""create owner column in posts

Revision ID: f9b30adeb10e
Revises: a95b67a29999
Create Date: 2022-03-12 10:51:38.014958

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f9b30adeb10e'
down_revision = 'a95b67a29999'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_user_fkey', source_table='posts', referent_table='users',
                        local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('post_user_fkey', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
