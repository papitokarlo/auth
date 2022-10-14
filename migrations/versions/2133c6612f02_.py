"""empty message

Revision ID: 2133c6612f02
Revises: 9d3141edd76a
Create Date: 2022-09-11 14:32:29.514847

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2133c6612f02'
down_revision = '9d3141edd76a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_post_heading', table_name='post')
    op.drop_table('post')
    op.drop_table('correct')
    op.drop_table('like')
    op.drop_index('ix_tag_name', table_name='tag')
    op.drop_table('tag')
    op.drop_table('comment')
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
    op.create_table('comment',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('text', sa.VARCHAR(length=200), nullable=False),
    sa.Column('date_created', sa.DATETIME(), nullable=True),
    sa.Column('author', sa.INTEGER(), nullable=False),
    sa.Column('post_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['author'], ['user.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['post_id'], ['post.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tag',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=15), nullable=False),
    sa.Column('date_created', sa.DATETIME(), nullable=True),
    sa.Column('author', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['author'], ['user.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_tag_name', 'tag', ['name'], unique=False)
    op.create_table('like',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('date_created', sa.DATETIME(), nullable=True),
    sa.Column('author', sa.INTEGER(), nullable=False),
    sa.Column('post_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['author'], ['user.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['post_id'], ['post.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('correct',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('date_created', sa.DATETIME(), nullable=True),
    sa.Column('author', sa.INTEGER(), nullable=False),
    sa.Column('post_id', sa.INTEGER(), nullable=False),
    sa.Column('comment_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['author'], ['user.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['comment_id'], ['comment.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['post_id'], ['post.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('post',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('heading', sa.VARCHAR(length=50), nullable=False),
    sa.Column('text', sa.TEXT(), nullable=False),
    sa.Column('date_created', sa.DATETIME(), nullable=True),
    sa.Column('tags', sa.VARCHAR(), nullable=False),
    sa.Column('author', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['author'], ['user.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['tags'], ['tag.name'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_post_heading', 'post', ['heading'], unique=False)
    # ### end Alembic commands ###