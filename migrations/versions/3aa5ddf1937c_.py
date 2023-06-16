"""empty message

Revision ID: 3aa5ddf1937c
Revises: 
Create Date: 2023-06-16 19:04:20.146980

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3aa5ddf1937c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('state', sa.Enum('NUEVO', 'SEMINUEVO', name='productstate'), nullable=False),
    sa.Column('price', sa.String(length=999999), nullable=False),
    sa.Column('description', sa.String(length=2000), nullable=True),
    sa.Column('images', sa.String(length=400), nullable=True),
    sa.Column('year', sa.Integer(), nullable=True),
    sa.Column('km', sa.Integer(), nullable=True),
    sa.Column('fuel', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('surname', sa.String(length=40), nullable=False),
    sa.Column('email', sa.String(length=80), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.Column('id_document', sa.Enum('DNI', 'CIF', name='iddocument'), nullable=False),
    sa.Column('id_number', sa.String(length=10), nullable=False),
    sa.Column('address', sa.String(length=120), nullable=False),
    sa.Column('role', sa.Enum('BUYER', 'SELLER', 'GARAGE', name='userrole'), nullable=False),
    sa.Column('phone', sa.Integer(), nullable=False),
    sa.Column('dark_mode', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('id_number')
    )
    op.create_table('favorites',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('favorites')
    op.drop_table('user')
    op.drop_table('product')
    # ### end Alembic commands ###