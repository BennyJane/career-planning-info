"""empty message

Revision ID: 18c18226284c
Revises: 
Create Date: 2020-11-24 19:58:04.010540

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '18c18226284c'
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
    op.create_table('stat_browse',
    sa.Column('id', sa.String(length=32), nullable=False),
    sa.Column('ip', sa.String(length=120), nullable=True),
    sa.Column('origin', sa.String(length=120), nullable=True, comment='网站视图函数名称'),
    sa.Column('create_at', sa.DateTime(), nullable=True),
    sa.Column('update_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('stat_info',
    sa.Column('id', sa.String(length=32), nullable=False),
    sa.Column('ip', sa.String(length=120), nullable=True),
    sa.Column('action', sa.String(length=32), nullable=True, comment='访客行为: like-点赞, download-下载'),
    sa.Column('count', sa.INTEGER(), nullable=True, comment='统计单个IP下载次数'),
    sa.Column('create_at', sa.DateTime(), nullable=True),
    sa.Column('update_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('warning_para',
    sa.Column('id', sa.String(length=32), nullable=False),
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
    op.drop_table('stat_browse')
    op.drop_table('point')
    op.drop_table('job_info')
    # ### end Alembic commands ###
