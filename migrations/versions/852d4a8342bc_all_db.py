"""all db

Revision ID: 852d4a8342bc
Revises: 
Create Date: 2020-07-24 11:02:06.364748

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '852d4a8342bc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('direction',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('point_of_departure', sa.String(), nullable=True),
    sa.Column('point_of_destination', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('manufacturer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('phase_of_flight',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('token', sa.String(length=32), nullable=True),
    sa.Column('token_expiration', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_token'), 'user', ['token'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.create_table('model',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('id_manufacturer', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_manufacturer'], ['manufacturer.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('board',
    sa.Column('registration_number', sa.String(), nullable=False),
    sa.Column('id_model', sa.Integer(), nullable=True),
    sa.Column('year_of_manufacture', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_model'], ['model.id'], ),
    sa.PrimaryKeyConstraint('registration_number')
    )
    op.create_table('flight',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_board', sa.String(), nullable=True),
    sa.Column('id_direction', sa.Integer(), nullable=True),
    sa.Column('time_begin', sa.Time(), nullable=True),
    sa.Column('date_begin', sa.Date(), nullable=True),
    sa.ForeignKeyConstraint(['id_board'], ['board.registration_number'], ),
    sa.ForeignKeyConstraint(['id_direction'], ['direction.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('subsystem',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('id_board', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['id_board'], ['board.registration_number'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_subsystem_name'), 'subsystem', ['name'], unique=False)
    op.create_table('duration_of_phase',
    sa.Column('id_flight', sa.Integer(), nullable=True),
    sa.Column('id_phase', sa.Integer(), nullable=True),
    sa.Column('start_phase', sa.Time(), nullable=True),
    sa.Column('end_phase', sa.Time(), nullable=True),
    sa.ForeignKeyConstraint(['id_flight'], ['flight.id'], ),
    sa.ForeignKeyConstraint(['id_phase'], ['phase_of_flight.id'], )
    )
    op.create_table('parameter',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('id_system', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_system'], ['subsystem.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_parameter_name'), 'parameter', ['name'], unique=False)
    op.create_table('parameter_value',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_parameter', sa.Integer(), nullable=True),
    sa.Column('time', sa.Time(), nullable=True),
    sa.Column('value', sa.Float(), nullable=True),
    sa.Column('id_flight', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_flight'], ['flight.id'], ),
    sa.ForeignKeyConstraint(['id_parameter'], ['parameter.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_parameter_value_time'), 'parameter_value', ['time'], unique=False)
    op.create_index(op.f('ix_parameter_value_value'), 'parameter_value', ['value'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_parameter_value_value'), table_name='parameter_value')
    op.drop_index(op.f('ix_parameter_value_time'), table_name='parameter_value')
    op.drop_table('parameter_value')
    op.drop_index(op.f('ix_parameter_name'), table_name='parameter')
    op.drop_table('parameter')
    op.drop_table('duration_of_phase')
    op.drop_index(op.f('ix_subsystem_name'), table_name='subsystem')
    op.drop_table('subsystem')
    op.drop_table('flight')
    op.drop_table('board')
    op.drop_table('model')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_token'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_table('phase_of_flight')
    op.drop_table('manufacturer')
    op.drop_table('direction')
    # ### end Alembic commands ###