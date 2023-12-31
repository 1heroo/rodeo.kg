"""little changes

Revision ID: 53e6f629680c
Revises: b19558f4bf27
Create Date: 2023-06-24 14:21:46.033594

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '53e6f629680c'
down_revision = 'b19558f4bf27'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tournament_events', sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True))
    op.add_column('tournaments', sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tournaments', 'created_at')
    op.drop_column('tournament_events', 'created_at')
    # ### end Alembic commands ###
