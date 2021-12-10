"""empty message

Revision ID: a3229957a46f
Revises: 
Create Date: 2021-12-07 17:03:18.116143

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a3229957a46f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('signals',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('td_up', sa.Float(), nullable=True),
    sa.Column('td_down', sa.Float(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('ohlc', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_signals_id'), 'signals', ['id'], unique=False)
    op.create_table('subscriptions',
    sa.Column('ticker', sa.String(), nullable=False),
    sa.Column('timeframe', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('ticker', 'timeframe')
    )
    op.create_table('test',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('message', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_test_id'), 'test', ['id'], unique=False)
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('_password', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    op.create_table('ohlc_data',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('open', sa.Float(), nullable=True),
    sa.Column('high', sa.Float(), nullable=True),
    sa.Column('low', sa.Float(), nullable=True),
    sa.Column('close', sa.Float(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('ticker', sa.String(), nullable=True),
    sa.Column('timeframe', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['ticker', 'timeframe'], ['subscriptions.ticker', 'subscriptions.timeframe'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_ohlc_data_id'), 'ohlc_data', ['id'], unique=False)
    op.create_table('user_subscriptions',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user', sa.Integer(), nullable=True),
    sa.Column('ticker', sa.String(), nullable=True),
    sa.Column('timeframe', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['ticker', 'timeframe'], ['subscriptions.ticker', 'subscriptions.timeframe'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_subscriptions_id'), 'user_subscriptions', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_subscriptions_id'), table_name='user_subscriptions')
    op.drop_table('user_subscriptions')
    op.drop_index(op.f('ix_ohlc_data_id'), table_name='ohlc_data')
    op.drop_table('ohlc_data')
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_test_id'), table_name='test')
    op.drop_table('test')
    op.drop_table('subscriptions')
    op.drop_index(op.f('ix_signals_id'), table_name='signals')
    op.drop_table('signals')
    # ### end Alembic commands ###
