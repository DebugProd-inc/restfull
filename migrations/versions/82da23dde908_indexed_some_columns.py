"""indexed some columns

Revision ID: 82da23dde908
Revises: 42a568221e9b
Create Date: 2020-07-14 08:53:48.740491

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '82da23dde908'
down_revision = '42a568221e9b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_parameter_name'), 'parameter', ['name'], unique=False)
    op.create_index(op.f('ix_parameter_value_time'), 'parameter_value', ['time'], unique=False)
    op.create_index(op.f('ix_parameter_value_value'), 'parameter_value', ['value'], unique=False)
    op.create_index(op.f('ix_subsystem_name'), 'subsystem', ['name'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_subsystem_name'), table_name='subsystem')
    op.drop_index(op.f('ix_parameter_value_value'), table_name='parameter_value')
    op.drop_index(op.f('ix_parameter_value_time'), table_name='parameter_value')
    op.drop_index(op.f('ix_parameter_name'), table_name='parameter')
    # ### end Alembic commands ###
