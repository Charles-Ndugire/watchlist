"""empty message

Revision ID: 844fa68e1b76
Revises: d02ac0c98b1d
Create Date: 2017-09-11 11:32:31.629201

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '844fa68e1b76'
down_revision = 'd02ac0c98b1d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('bio', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('profile_pic_path', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'profile_pic_path')
    op.drop_column('users', 'bio')
    # ### end Alembic commands ###
