"""empty message

Revision ID: bc961267b82a
Revises: d594190d8c7c
Create Date: 2020-11-19 15:08:27.552609

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bc961267b82a'
down_revision = 'd594190d8c7c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('stat_browse',
    sa.Column('id', sa.String(length=32), nullable=False),
    sa.Column('page_views', sa.BigInteger(), nullable=True),
    sa.Column('origin', sa.String(length=120), nullable=True, comment='网站视图函数名称'),
    sa.Column('create_at', sa.DateTime(), nullable=True),
    sa.Column('update_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('stat_browse')
    # ### end Alembic commands ###
