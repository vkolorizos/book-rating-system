"""initial tables

Revision ID: 1ffd597188cc
Revises: 
Create Date: 2022-11-16 13:49:20.828161

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1ffd597188cc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('book_reviews',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('book_id', sa.Integer(), nullable=True),
    sa.Column('rating', sa.Integer(), nullable=True),
    sa.Column('comment', sa.Text(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('book_reviews', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_book_reviews_book_id'), ['book_id'], unique=True)
        batch_op.create_index(batch_op.f('ix_book_reviews_id'), ['id'], unique=False)

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('book_reviews', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_book_reviews_id'))
        batch_op.drop_index(batch_op.f('ix_book_reviews_book_id'))

    op.drop_table('book_reviews')
    # ### end Alembic commands ###
