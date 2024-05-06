"""Remove some constraint

Revision ID: 9081c6d57791
Revises: 
Create Date: 2024-05-06 22:23:11.034482

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9081c6d57791'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('conferences',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('conferenceId', sa.String(length=10), nullable=False),
    sa.Column('city', sa.String(length=100), nullable=False),
    sa.Column('deadline', sa.String(length=100), nullable=True),
    sa.Column('date', sa.String(length=100), nullable=True),
    sa.Column('notification', sa.String(length=100), nullable=True),
    sa.Column('submission', sa.String(length=1000), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('conferencesDetails',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('conferenceId', sa.String(length=10), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('website', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('conferencesFuture',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('conferenceId', sa.String(length=10), nullable=False),
    sa.Column('city', sa.String(length=100), nullable=False),
    sa.Column('date', sa.String(length=100), nullable=True),
    sa.Column('notification', sa.String(length=100), nullable=True),
    sa.Column('finalVersion', sa.String(length=1000), nullable=True),
    sa.Column('earlyRegistration', sa.String(length=100), nullable=True),
    sa.Column('remarks', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('conferencesPlanning',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('conferenceId', sa.String(length=10), nullable=False),
    sa.Column('Year', sa.Integer(), nullable=False),
    sa.Column('city', sa.String(length=100), nullable=False),
    sa.Column('startingDate', sa.String(length=100), nullable=True),
    sa.Column('endingDate', sa.String(length=100), nullable=True),
    sa.Column('remarks', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('conferencesRunning',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('conferenceId', sa.String(length=10), nullable=False),
    sa.Column('city', sa.String(length=100), nullable=False),
    sa.Column('date', sa.String(length=100), nullable=True),
    sa.Column('remarks', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('conferencesRunning')
    op.drop_table('conferencesPlanning')
    op.drop_table('conferencesFuture')
    op.drop_table('conferencesDetails')
    op.drop_table('conferences')
    # ### end Alembic commands ###