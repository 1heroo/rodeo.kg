"""little changes

Revision ID: 252203321f17
Revises: 53e6f629680c
Create Date: 2023-06-24 14:37:24.062941

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '252203321f17'
down_revision = '53e6f629680c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tournament_events', sa.Column('scroll', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tournament_events', 'scroll')
    # ### end Alembic commands ###