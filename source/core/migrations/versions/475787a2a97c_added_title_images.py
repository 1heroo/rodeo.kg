"""added title images

Revision ID: 475787a2a97c
Revises: 164fe0d1a009
Create Date: 2023-06-24 13:30:34.258705

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_fields
from sqlalchemy_fields.storages import FileSystemStorage

# revision identifiers, used by Alembic.
revision = '475787a2a97c'
down_revision = '164fe0d1a009'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('news_title',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title_ru', sa.String(), nullable=True),
    sa.Column('title_en', sa.String(), nullable=True),
    sa.Column('title_kg', sa.String(), nullable=True),
    sa.Column('image', sqlalchemy_fields.types.image.ImageType(storage=FileSystemStorage), nullable=True),
    sa.Column('image_url', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('gallery_title', sa.Column('image', sqlalchemy_fields.types.image.ImageType(storage=FileSystemStorage), nullable=True))
    op.add_column('gallery_title', sa.Column('image_url', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('gallery_title', 'image_url')
    op.drop_column('gallery_title', 'image')
    op.drop_table('news_title')
    # ### end Alembic commands ###
