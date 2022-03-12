"""create posts table

Revision ID: 866571b9e167
Revises: 
Create Date: 2022-03-12 10:23:27.598540

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '866571b9e167'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts',sa.Column('id', sa.Integer(), nullable=False, primary_key=True), 
                    sa.Column('title', sa.String(), nullable=False),
                    sa.Column('content', sa.String, nullable=False),
                    sa.Column('published', sa.Boolean, server_default='True',nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),nullable=False,
                              server_default=sa.text('NOW()')),
                    sa.PrimaryKeyConstraint('id')        
                    )
    pass


def downgrade():
    op.drop_table('posts')
    pass
