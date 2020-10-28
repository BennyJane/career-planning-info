"""empty message

Revision ID: f519d9f35e70
Revises: 
Create Date: 2020-10-28 23:03:30.725013

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f519d9f35e70'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('job_info',
    sa.Column('id', sa.String(length=32), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.Column('salary', sa.Integer(), nullable=False),
    sa.Column('year', sa.String(length=32), nullable=False),
    sa.Column('site', sa.String(length=32), nullable=False),
    sa.Column('responsibility', sa.Text(), nullable=False),
    sa.Column('demand', sa.Text(), nullable=False),
    sa.Column('other', sa.Text(), nullable=False),
    sa.Column('source', sa.Text(), nullable=False),
    sa.Column('source_id', sa.String(length=32), nullable=False),
    sa.Column('source_url', sa.Text(), nullable=False),
    sa.Column('create_at', sa.DateTime(), nullable=True),
    sa.Column('update_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('point',
    sa.Column('id', sa.String(length=32), nullable=False),
    sa.Column('salary', sa.Integer(), nullable=True),
    sa.Column('site', sa.String(length=32), nullable=True),
    sa.Column('year', sa.String(length=32), nullable=True),
    sa.Column('requirement', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('point')
    op.drop_table('job_info')
    # ### end Alembic commands ###