"""add model users

Revision ID: 146691a88df6
Revises: e254f440704c
Create Date: 2024-01-16 15:59:34.164971

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '146691a88df6'
down_revision = 'e254f440704c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('hashed_password', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
