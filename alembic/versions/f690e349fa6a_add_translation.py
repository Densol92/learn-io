"""add translation

Revision ID: f690e349fa6a
Revises: a10dfa978f7d
Create Date: 2021-11-21 21:13:43.809487

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f690e349fa6a'
down_revision = 'a10dfa978f7d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('translation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('word', sa.Integer(), nullable=False),
    sa.Column('translation', sa.Integer(), nullable=False),
    sa.Column('popularity', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['translation'], ['word.id'], ),
    sa.ForeignKeyConstraint(['word'], ['word.id'], ),
    sa.PrimaryKeyConstraint('id', 'word', 'translation')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('translation')
    # ### end Alembic commands ###
