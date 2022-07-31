"""authentication

Revision ID: e685481aae84
Revises: 
Create Date: 2022-07-30 17:39:45.907837

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e685481aae84'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_fullname'), 'users', ['fullname'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_fullname'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    # ### end Alembic commands ###