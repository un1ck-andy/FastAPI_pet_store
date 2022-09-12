"""initial

Revision ID: 82127f59a4cd
Revises:
Create Date: 2022-07-31 22:38:07.686846

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '82127f59a4cd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('username', sa.String(), nullable=True),
                    sa.Column('email', sa.String(), nullable=True),
                    sa.Column('password', sa.String(), nullable=True),
                    sa.Column('phone', sa.String(), nullable=True),
                    sa.Column('first_name', sa.String(), nullable=True),
                    sa.Column('last_name', sa.String(), nullable=True),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email'),
                    sa.UniqueConstraint('phone')
                    )
    op.create_index(op.f('ix_users_login'), 'users', ['username'], unique=True)
    op.create_table('pet',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(), nullable=True),
                    sa.Column('status', sa.String(), nullable=True),
                    sa.Column('category', postgresql.JSON(astext_type=sa.Text()), nullable=True),
                    sa.Column('user_id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete="CASCADE"),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_pet_name'), 'pet', ['name'], unique=False)
    op.create_table('store',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('pet_id', sa.Integer(), nullable=True),
                    sa.Column('quantity', sa.Integer(), nullable=True),
                    sa.Column('status', sa.String(), nullable=True),
                    sa.Column('complete', sa.Boolean(), nullable=True),
                    sa.ForeignKeyConstraint(['pet_id'], ['pet.id'], ondelete="CASCADE"),
                    sa.PrimaryKeyConstraint('id')
                    )


def downgrade():
    op.drop_table('store')
    op.drop_table('pet')
    op.drop_index(op.f('ix_users_login'), table_name='users')
    op.drop_table('users')
