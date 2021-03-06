"""empty message

Revision ID: d2ac27de2305
Revises: 5a60da91cb5d
Create Date: 2021-01-11 22:00:40.079804

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'd2ac27de2305'
down_revision = '5a60da91cb5d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('message', 'body',
               existing_type=mysql.TEXT(charset='utf8mb4', collation='utf8mb4_unicode_ci'),
               comment='留言内容',
               existing_nullable=True)
    op.alter_column('stat_browse', 'update_at',
               existing_type=mysql.DATETIME(),
               nullable=False)
    op.alter_column('stat_info', 'update_at',
               existing_type=mysql.DATETIME(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('stat_info', 'update_at',
               existing_type=mysql.DATETIME(),
               nullable=True)
    op.alter_column('stat_browse', 'update_at',
               existing_type=mysql.DATETIME(),
               nullable=True)
    op.alter_column('message', 'body',
               existing_type=mysql.TEXT(charset='utf8mb4', collation='utf8mb4_unicode_ci'),
               comment=None,
               existing_comment='留言内容',
               existing_nullable=True)
    # ### end Alembic commands ###
