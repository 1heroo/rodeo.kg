"""initial

Revision ID: 5281deac1c0e
Revises: 
Create Date: 2023-06-12 21:56:01.173452

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_fields
from sqlalchemy_fields.types import ImageType
from sqlalchemy_fields.storages import FileSystemStorage


# revision identifiers, used by Alembic.
revision = '5281deac1c0e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('images',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('image', sqlalchemy_fields.types.image.ImageType(
        storage=FileSystemStorage), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('news',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('image', sqlalchemy_fields.types.image.ImageType(storage=FileSystemStorage), nullable=True),
    sa.Column('upper_title_ru', sa.String(), nullable=True),
    sa.Column('upper_title_kg', sa.String(), nullable=True),
    sa.Column('upper_title_en', sa.String(), nullable=True),
    sa.Column('title_ru', sa.String(), nullable=True),
    sa.Column('title_kg', sa.String(), nullable=True),
    sa.Column('title_en', sa.String(), nullable=True),
    sa.Column('description_ru', sa.String(), nullable=True),
    sa.Column('description_kg', sa.String(), nullable=True),
    sa.Column('description_en', sa.String(), nullable=True),
    sa.Column('location_n_date_ru', sa.String(), nullable=True),
    sa.Column('location_n_date_kg', sa.String(), nullable=True),
    sa.Column('location_n_date_en', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('news')
    op.drop_table('images')
    # ### end Alembic commands ###
