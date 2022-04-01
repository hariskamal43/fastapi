"""create users table

Revision ID: a95b67a29999
Revises: 866571b9e167
Create Date: 2022-03-12 10:37:56.790933

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a95b67a29999'
down_revision = '866571b9e167'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.Column('username', sa.String(), nullable=False, unique=True),
                    sa.Column('email', sa.String(), nullable=False, unique=True),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email', 'username')                
    )
    pass


def downgrade():
    op.drop_table('users')
    pass
