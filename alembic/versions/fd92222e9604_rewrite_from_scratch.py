"""rewrite from scratch

Revision ID: fd92222e9604
Revises: f690e349fa6a
Create Date: 2021-11-23 20:42:16.211528

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fd92222e9604'
down_revision = 'f690e349fa6a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('translation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('word_id', sa.Integer(), nullable=True),
    sa.Column('translation', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['word_id'], ['word.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('translation')
    # ### end Alembic commands ###