"""add a colum

Revision ID: 8d621d73559d
Revises: 
Create Date: 2023-04-04 10:07:31.688758

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '8d621d73559d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    pass
    # after these codes runs it immediately takes effect in the database and if we try to run it again it shows
    # duplicate column entry so in situations where we need to run downgrade or upgrade again, we need to comment out
    # these codes and use the 'pass' statement
    op.add_column("person", sa.Column("email", sa.String(30)))  # add 'email' column in the person table
    op.add_column("user", sa.Column("person_id", sa.BIGINT()))



def downgrade() -> None:
    pass
    op.drop_column("person", 'email')  # delete 'email' column in the person table
    op.drop_column("user", 'person_id')

