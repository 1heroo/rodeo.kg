"""added gallery_staff

Revision ID: 164fe0d1a009
Revises: 0aac590b651d
Create Date: 2023-06-24 12:34:40.084351

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
import sqlalchemy_fields
from sqlalchemy_fields.storages import FileSystemStorage

# revision identifiers, used by Alembic.
revision = '164fe0d1a009'
down_revision = '0aac590b651d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('gallery_images',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('image', sqlalchemy_fields.types.image.ImageType(storage=FileSystemStorage), nullable=True),
    sa.Column('image_url', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('scroll', sa.Boolean(), nullable=True),
    sa.Column('upper_part', sa.Boolean(), nullable=True),
    sa.Column('lower_part', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('gallery_title',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('page_title_ru', sa.String(), nullable=True),
    sa.Column('page_title_en', sa.String(), nullable=True),
    sa.Column('page_title_kg', sa.String(), nullable=True),
    sa.Column('upper_title_en', sa.String(), nullable=True),
    sa.Column('upper_title_ru', sa.String(), nullable=True),
    sa.Column('upper_title_kg', sa.String(), nullable=True),
    sa.Column('lower_title_ru', sa.String(), nullable=True),
    sa.Column('lower_title_en', sa.String(), nullable=True),
    sa.Column('lower_title_kg', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('images')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('images',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('image', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(), server_default=sa.text('now()'), autoincrement=False, nullable=True),
    sa.Column('image_url', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='images_pkey')
    )
    op.drop_table('gallery_title')
    op.drop_table('gallery_images')
    # ### end Alembic commands ###
