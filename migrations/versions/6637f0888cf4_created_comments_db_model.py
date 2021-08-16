"""Created comments db model

Revision ID: 6637f0888cf4
Revises: fa4f694e986a
Create Date: 2021-08-16 21:50:54.809901

"""

# revision identifiers, used by Alembic.
revision = '6637f0888cf4'
down_revision = 'fa4f694e986a'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('comment', sa.String(length=64), nullable=True),
    sa.Column('pitches_id', sa.Integer(), nullable=True),
    sa.Column('time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['pitches_id'], ['pitches.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comments')
    # ### end Alembic commands ###