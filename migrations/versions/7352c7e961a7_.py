"""empty message

Revision ID: 7352c7e961a7
Revises: 671162641299
Create Date: 2019-07-24 10:47:52.629088

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7352c7e961a7'
down_revision = '671162641299'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('movies', sa.Column('rating', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('movies', 'rating')
    # ### end Alembic commands ###
