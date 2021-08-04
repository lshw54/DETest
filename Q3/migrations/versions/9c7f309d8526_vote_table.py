"""Vote Table

Revision ID: 9c7f309d8526
Revises: 
Create Date: 2021-08-04 01:26:42.505218

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9c7f309d8526'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('vote',
    sa.Column('vote_id', sa.Integer(), nullable=False),
    sa.Column('candidates', sa.Text(), nullable=True),
    sa.Column('datetime', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('vote_id')
    )
    op.create_index(op.f('ix_vote_datetime'), 'vote', ['datetime'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_vote_datetime'), table_name='vote')
    op.drop_table('vote')
    # ### end Alembic commands ###