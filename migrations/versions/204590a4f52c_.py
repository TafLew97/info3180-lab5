"""empty message

Revision ID: 204590a4f52c
Revises: e4a129bc0b12
Create Date: 2019-03-04 01:39:14.651815

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '204590a4f52c'
down_revision = 'e4a129bc0b12'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_profiles', sa.Column('password', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_profiles', 'password')
    # ### end Alembic commands ###
