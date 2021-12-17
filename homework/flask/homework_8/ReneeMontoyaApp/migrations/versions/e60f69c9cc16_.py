"""empty message

Revision ID: e60f69c9cc16
Revises: 97acf0014585
Create Date: 2021-12-14 12:38:34.058903

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'e60f69c9cc16'
down_revision = '97acf0014585'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('employees', 'department_id',
               existing_type=mysql.INTEGER(),
               nullable=True)
    op.create_foreign_key(None, 'employees', 'plants', ['department_id'], ['id'])
    op.create_foreign_key(None, 'plants', 'employees', ['director_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'plants', type_='foreignkey')
    op.drop_constraint(None, 'employees', type_='foreignkey')
    op.alter_column('employees', 'department_id',
               existing_type=mysql.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###