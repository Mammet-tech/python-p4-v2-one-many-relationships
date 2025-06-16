"""add foreign key to onboarding

Revision ID: 0d246ded1255
Revises: a8e065c7d95d
Create Date: 2025-06-16 13:41:26.425989
"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0d246ded1255'
down_revision = 'a8e065c7d95d'
branch_labels = None
depends_on = None


def upgrade():
    # ### use batch mode for SQLite compatibility ###
    with op.batch_alter_table('onboardings', schema=None) as batch_op:
        batch_op.add_column(sa.Column('employee_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(
            batch_op.f('fk_onboardings_employee_id_employees'),
            'employees',
            ['employee_id'],
            ['id']
        )


def downgrade():
    # ### reverse using batch mode ###
    with op.batch_alter_table('onboardings', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_onboardings_employee_id_employees'), type_='foreignkey')
        batch_op.drop_column('employee_id')
