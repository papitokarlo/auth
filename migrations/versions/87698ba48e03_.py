"""empty message

Revision ID: 87698ba48e03
Revises: 
Create Date: 2022-08-30 19:55:19.719427

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '87698ba48e03'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_user_email', table_name='user')
    op.drop_index('ix_user_fullname', table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('fullname', sa.VARCHAR(length=200), nullable=False),
    sa.Column('email', sa.VARCHAR(length=100), nullable=False),
    sa.Column('linkedin', sa.VARCHAR(length=50), nullable=False),
    sa.Column('github', sa.VARCHAR(length=45), nullable=False),
    sa.Column('date_created', sa.DATETIME(), nullable=True),
    sa.Column('password_hash', sa.VARCHAR(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('github'),
    sa.UniqueConstraint('linkedin')
    )
    op.create_index('ix_user_fullname', 'user', ['fullname'], unique=False)
    op.create_index('ix_user_email', 'user', ['email'], unique=False)
    # ### end Alembic commands ###
