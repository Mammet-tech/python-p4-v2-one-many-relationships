"""add foreign key to Review

Revision ID: a8e065c7d95d
Revises: f574635f034b
Create Date: 2025-06-16 11:54:19.848964

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a8e065c7d95d'
down_revision = 'f574635f034b'
branch_labels = None
depends_on = None


def upgrade():
    # Use batch_alter_table for SQLite compatibility
    with op.batch_alter_table('reviews', schema=None) as batch_op:
        batch_op.add_column(sa.Column('employee_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(
            batch_op.f('fk_reviews_employee_id_employees'),
            'employees',
            ['employee_id'],
            ['id']
        )


def downgrade():
    with op.batch_alter_table('reviews', schema=None) as batch_op:
        batch_op.drop_constraint(
            batch_op.f('fk_reviews_employee_id_employees'),
            type_='foreignkey'
        )
        batch_op.drop_column('employee_id')
