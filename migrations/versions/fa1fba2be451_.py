"""empty message

Revision ID: fa1fba2be451
Revises: None
Create Date: 2016-10-16 05:39:05.292714

"""

# revision identifiers, used by Alembic.
revision = 'fa1fba2be451'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=100), nullable=True),
    sa.Column('password', sa.String(length=100), nullable=True),
    sa.Column('role', sa.Integer(), nullable=True),
    sa.Column('signature', sa.String(length=100), nullable=True),
    sa.Column('visit', sa.Integer(), nullable=True),
    sa.Column('sex', sa.String(length=100), nullable=True),
    sa.Column('ip', sa.String(length=100), nullable=True),
    sa.Column('created_time', sa.String(length=100), nullable=True),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('tweets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.String(length=100), nullable=True),
    sa.Column('created_time', sa.String(length=100), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.String(length=100), nullable=True),
    sa.Column('created_time', sa.String(length=100), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('tweet_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['tweet_id'], ['tweets.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comments')
    op.drop_table('tweets')
    op.drop_table('users')
    ### end Alembic commands ###
