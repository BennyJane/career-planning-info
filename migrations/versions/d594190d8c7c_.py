"""empty message

Revision ID: d594190d8c7c
Revises: f519d9f35e70
Create Date: 2020-11-19 13:44:30.189694

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd594190d8c7c'
down_revision = 'f519d9f35e70'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('stat_info',
    sa.Column('id', sa.String(length=32), autoincrement=True, nullable=False),
    sa.Column('ip', sa.String(length=120), nullable=True),
    sa.Column('link', sa.Boolean(), nullable=True),
    sa.Column('download', sa.Boolean(), nullable=True),
    sa.Column('create_at', sa.DateTime(), nullable=True),
    sa.Column('update_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('warning_para',
    sa.Column('id', sa.String(length=32), autoincrement=True, nullable=False),
    sa.Column('para', sa.Text(), nullable=True),
    sa.Column('create_at', sa.DateTime(), nullable=True),
    sa.Column('update_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('warning_para')
    op.drop_table('stat_info')
    # ### end Alembic commands ###