"""add new tables for data-manager-api

Revision ID: 94e1f03da9e4
Revises: b146f67ebe1f
Create Date: 2024-05-26 13:23:20.066017

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '94e1f03da9e4'
down_revision: Union[str, None] = 'b146f67ebe1f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('certifications',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('issuing_organization', sa.String(), nullable=True),
    sa.Column('issue_date', sa.String(), nullable=True),
    sa.Column('expiration_date', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_certifications_id'), 'certifications', ['id'], unique=False)
    op.create_index(op.f('ix_certifications_name'), 'certifications', ['name'], unique=False)
    op.create_table('contacts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('phone', sa.String(), nullable=True),
    sa.Column('address', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_contacts_email'), 'contacts', ['email'], unique=False)
    op.create_index(op.f('ix_contacts_id'), 'contacts', ['id'], unique=False)
    op.create_table('past_experiences',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('company', sa.String(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('start_date', sa.String(), nullable=True),
    sa.Column('end_date', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_past_experiences_id'), 'past_experiences', ['id'], unique=False)
    op.create_index(op.f('ix_past_experiences_title'), 'past_experiences', ['title'], unique=False)
    op.create_table('programming_skills',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('level', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_programming_skills_id'), 'programming_skills', ['id'], unique=False)
    op.create_index(op.f('ix_programming_skills_name'), 'programming_skills', ['name'], unique=False)
    op.create_table('resumes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('profile_id', sa.Integer(), nullable=True),
    sa.Column('file_path', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_resumes_id'), 'resumes', ['id'], unique=False)
    op.create_index(op.f('ix_resumes_profile_id'), 'resumes', ['profile_id'], unique=False)
    op.create_table('soft_skills',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_soft_skills_id'), 'soft_skills', ['id'], unique=False)
    op.create_index(op.f('ix_soft_skills_name'), 'soft_skills', ['name'], unique=False)
    op.create_table('tech_stacks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_tech_stacks_id'), 'tech_stacks', ['id'], unique=False)
    op.create_index(op.f('ix_tech_stacks_name'), 'tech_stacks', ['name'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_tech_stacks_name'), table_name='tech_stacks')
    op.drop_index(op.f('ix_tech_stacks_id'), table_name='tech_stacks')
    op.drop_table('tech_stacks')
    op.drop_index(op.f('ix_soft_skills_name'), table_name='soft_skills')
    op.drop_index(op.f('ix_soft_skills_id'), table_name='soft_skills')
    op.drop_table('soft_skills')
    op.drop_index(op.f('ix_resumes_profile_id'), table_name='resumes')
    op.drop_index(op.f('ix_resumes_id'), table_name='resumes')
    op.drop_table('resumes')
    op.drop_index(op.f('ix_programming_skills_name'), table_name='programming_skills')
    op.drop_index(op.f('ix_programming_skills_id'), table_name='programming_skills')
    op.drop_table('programming_skills')
    op.drop_index(op.f('ix_past_experiences_title'), table_name='past_experiences')
    op.drop_index(op.f('ix_past_experiences_id'), table_name='past_experiences')
    op.drop_table('past_experiences')
    op.drop_index(op.f('ix_contacts_id'), table_name='contacts')
    op.drop_index(op.f('ix_contacts_email'), table_name='contacts')
    op.drop_table('contacts')
    op.drop_index(op.f('ix_certifications_name'), table_name='certifications')
    op.drop_index(op.f('ix_certifications_id'), table_name='certifications')
    op.drop_table('certifications')
    # ### end Alembic commands ###
