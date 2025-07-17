"""add seo_description to blog_posts

Revision ID: add_seo_description
Revises: 4a29c1078ab7
Create Date: 2024-06-XX XX:XX:XX.XXXXXX

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'add_seo_description'
down_revision = '4a29c1078ab7'
branch_labels = None
depends_on = None

def upgrade():
    op.add_column('blog_posts', sa.Column('seo_description', sa.String(length=160), nullable=True))

def downgrade():
    op.drop_column('blog_posts', 'seo_description')