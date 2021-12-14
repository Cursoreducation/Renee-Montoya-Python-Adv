"""empty message

Revision ID: 97acf0014585
Revises: 4d78fc9117d2
Create Date: 2021-12-13 10:54:06.333509

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '97acf0014585'
down_revision = '4d78fc9117d2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('employees', 'department_type',
               existing_type=mysql.VARCHAR(length=50),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('employees', 'department_type',
               existing_type=mysql.VARCHAR(length=50),
               nullable=False)
    # ### end Alembic commands ###
