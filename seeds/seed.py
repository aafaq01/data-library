import sys
import os

# Add the parent directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import sys
import os
import datetime
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models.profile import Profile
from models.project import Project
from models.certification import Certification
from models.contact import Contact
from models.past_experience import PastExperience
from models.programming_skill import ProgrammingSkill
from models.resume import Resume
from models.soft_skill import SoftSkill
from models.tech_stack import TechStack
from settings import settings

# Add the parent directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Replace this with your actual database URL
DATABASE_URL = settings.database_url

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

def remove_data():
    """Remove all seed data from the database."""
    session.query(Certification).delete()
    session.query(Contact).delete()
    session.query(PastExperience).delete()
    session.query(ProgrammingSkill).delete()
    session.query(Resume).delete()
    session.query(SoftSkill).delete()
    session.query(TechStack).delete()
    session.query(Project).delete()
    session.query(Profile).delete()
    session.commit()
    print("All seed data removed successfully!")

def seed_data():
    remove_data()

    # Creating a profile
    profile = Profile(
        name='John Doe',
        description='Senior DevOps Engineer with 7+ years of experience in automating deployments and managing infrastructure.'
    )
    session.add(profile)
    session.commit()

    # Creating projects
    projects = [
        Project(
            name='CI/CD Pipeline Automation',
            description='Developed a fully automated CI/CD pipeline using Jenkins, Docker, and Kubernetes.',
            profile_id=profile.id
        ),
        Project(
            name='Cloud Infrastructure Optimization',
            description='Optimized cloud infrastructure for cost and performance using Terraform and AWS.',
            profile_id=profile.id
        ),
        Project(
            name='Monitoring and Logging System',
            description='Implemented a monitoring and logging system using Prometheus and Grafana.',
            profile_id=profile.id
        )
    ]
    session.add_all(projects)

    # Creating certifications
    certifications = [
        Certification(
            name='Certified Kubernetes Administrator (CKA)',
            issuing_organization='Cloud Native Computing Foundation',
            issue_date=datetime.date(2022, 1, 15),
            expiration_date=datetime.date(2024, 1, 15),
            profile_id=profile.id
        ),
        Certification(
            name='AWS Certified Solutions Architect',
            issuing_organization='Amazon Web Services',
            issue_date=datetime.date(2021, 5, 20),
            expiration_date=datetime.date(2024, 5, 20),
            profile_id=profile.id
        ),
        Certification(
            name='Google Cloud Professional DevOps Engineer',
            issuing_organization='Google Cloud',
            issue_date=datetime.date(2020, 8, 10),
            expiration_date=datetime.date(2023, 8, 10),
            profile_id=profile.id
        )
    ]
    session.add_all(certifications)

    # Creating contacts
    contact = Contact(
        email='john.doe@example.com',
        phone='555-1234',
        profile_id=profile.id
    )
    session.add(contact)

    # Creating past experiences
    past_experiences = [
        PastExperience(
            title='DevOps Engineer',
            company='Tech Solutions Inc.',
            start_date=datetime.date(2019, 3, 1),
            end_date=datetime.date(2022, 6, 30),
            description='Responsible for building and maintaining CI/CD pipelines and automating infrastructure.',
            profile_id=profile.id
        ),
        PastExperience(
            title='Senior DevOps Engineer',
            company='Innovative Cloud',
            start_date=datetime.date(2022, 7, 1),
            end_date=datetime.date(2024, 5, 1),
            description='Led a team of DevOps engineers to optimize cloud infrastructure and implement best practices.',
            profile_id=profile.id
        ),
        PastExperience(
            title='Systems Administrator',
            company='Cloud Services LLC',
            start_date=datetime.date(2016, 1, 15),
            end_date=datetime.date(2019, 2, 28),
            description='Managed and monitored cloud infrastructure and performed system upgrades.',
            profile_id=profile.id
        )
    ]
    session.add_all(past_experiences)

    # Creating programming skills
    programming_skills = [
        ProgrammingSkill(
            name='Python',
            level='Advanced',
            profile_id=profile.id
        ),
        ProgrammingSkill(
            name='Bash',
            level='Intermediate',
            profile_id=profile.id
        ),
        ProgrammingSkill(
            name='Go',
            level='Beginner',
            profile_id=profile.id
        ),
        ProgrammingSkill(
            name='JavaScript',
            level='Intermediate',
            profile_id=profile.id
        ),
        ProgrammingSkill(
            name='Ruby',
            level='Beginner',
            profile_id=profile.id
        )
    ]
    session.add_all(programming_skills)

    # Creating a resume
    resume = Resume(
        file_path='https://drive.google.com/file/d/1sODrpQwCyeq4VE7uLw-TrPdkoZSUw-BY/view?usp=drive_link',
        profile_id=profile.id,
    )
    session.add(resume)

    # Creating soft skills
    soft_skills = [
        SoftSkill(
            name='Communication',
            profile_id=profile.id
        ),
        SoftSkill(
            name='Team Collaboration',
            profile_id=profile.id
        ),
        SoftSkill(
            name='Problem Solving',
            profile_id=profile.id
        ),
        SoftSkill(
            name='Time Management',
            profile_id=profile.id
        ),
        SoftSkill(
            name='Leadership',
            profile_id=profile.id
        )
    ]
    session.add_all(soft_skills)

    # Creating tech stacks
    tech_stacks = [
        TechStack(
            name='Docker',
            profile_id=profile.id
        ),
        TechStack(
            name='Kubernetes',
            profile_id=profile.id
        ),
        TechStack(
            name='Terraform',
            profile_id=profile.id
        ),
        TechStack(
            name='Ansible',
            profile_id=profile.id
        ),
        TechStack(
            name='Jenkins',
            profile_id=profile.id
        ),
        TechStack(
            name='Prometheus',
            profile_id=profile.id
        ),
        TechStack(
            name='Grafana',
            profile_id=profile.id
        )
    ]
    session.add_all(tech_stacks)

    session.commit()
    print("Seed data added successfully!")

if __name__ == '__main__':
    seed_data()
