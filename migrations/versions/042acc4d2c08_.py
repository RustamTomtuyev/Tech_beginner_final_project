"""empty message

Revision ID: 042acc4d2c08
Revises: 0c0508f4e7e1
Create Date: 2023-06-08 03:33:32.763700

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '042acc4d2c08'
down_revision = '0c0508f4e7e1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('imagee',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('img', sa.String(length=150), nullable=False),
    sa.Column('proid', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['proid'], ['product.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('image')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('image',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('img', mysql.VARCHAR(length=150), nullable=False),
    sa.Column('proid', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['proid'], ['product.id'], name='image_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.drop_table('imagee')
    # ### end Alembic commands ###