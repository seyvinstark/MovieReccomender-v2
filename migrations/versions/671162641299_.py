"""empty message

Revision ID: 671162641299
Revises: 
Create Date: 2019-07-24 08:44:28.762123

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '671162641299'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('carts', sa.Column('status', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('carts', 'status')
    # ### end Alembic commands ###
