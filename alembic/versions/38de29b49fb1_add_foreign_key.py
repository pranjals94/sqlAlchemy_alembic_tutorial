"""add foreign key

Revision ID: 38de29b49fb1
Revises: 8d621d73559d
Create Date: 2023-04-04 10:32:54.757087

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '38de29b49fb1'
down_revision = '8d621d73559d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    pass
    op.create_foreign_key(
        'fk_name_person_user_relation',
        'user', 'person',
        ['person_id'], ['id']  # also can create multiple foreign keys
    )



def downgrade() -> None:
    pass
    op.drop_constraint(u'fk_name_person_user_relation', 'user', type_='foreignkey')