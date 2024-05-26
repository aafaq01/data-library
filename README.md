# data-library

Project Setup
1. Install Python - 3.12
2. Install Poetry - 1.7.1
3. Run command: "poetry shell" to enable virtual environment
4. Run command "poetry install" to install all the dependencies
5. Setup a .env file with original values as given in .dev.env
6. Alternatively, you can also set env variables using the command: "export VARIABLE=value" where VARIABLE is the variable name and value is its value

Run Migrations:
1. Run command to create a migration script:
    poetry run alembic revision --autogenerate -m "profile migration"
    (Use this command when there are no migration scripts in migrations/version folder or new models are defined and we need to generate the latest scripts)
2. Run command to apply the latest migrations on database
    poetry run alembic upgrade head

Some Alembic commands that can be used:
1. Check current migrations:
    poetry run alembic current
2. Revert all migrations:
    poetry run alembic downgrade base
3. Revert to last migration:
    poetry run alembic downgrade -1
4. Revert to a specific migrations:
    poetry run alembic downgrade <revision_name>
