"""add date column in comments table

Revision ID: a19abb99ac3a
Revises: ca2192e58314
Create Date: 2019-12-01 14:33:17.658715

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a19abb99ac3a'
down_revision = 'ca2192e58314'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('date', sa.DateTime(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('comments', 'date')
    # ### end Alembic commands ###