# Activity 8: Code quality

Code quality was covered in week 4.

This activity is a prompt to remind you.

Docstrings and exception handling have been omitted from the activities this week to keep focus on the queries but
should be considered when you write your coursework code.

Some SQLModel specific considerations:

1. Structure - refer to [SQLModel specific guidance](https://sqlmodel.tiangolo.com/tutorial/code-structure/?h=structure)
2. Docstrings for classes - refer to the guidance for the style you are using
   e.g. [Google style](https://google.github.io/styleguide/pyguide.html#384-classes)
3. Linting

   When you create the database you import models, yet the import is not explicitly used in the Python code. The linter
   will warn about this. It is an example of a situation you can ignore.

   Try `flake8 --max-line-length=100 src/activities/starter/db_wk8/database.py` in the terminal pane.

4. Exception handling in SQLModel

   SQLModel extends pydantic and SQLAlchemy so you would be handling Exceptions from these packages. Some of the common
   ones you might experience:

    - pydantic: ValidationError
    - sqlalchemy: IntegrityError, SQLAlchemyError (base class for sqlalchemy errors),
      OperationalError, [see documentation](https://docs.sqlalchemy.org/en/20/core/exceptions.html)

   Have a look at the following tutorials on Exception handling for these:

    - [Deal with Common Types of SQLAlchemy Exceptions for Running SQL Queries in Python](https://plainenglish.io/blog/deal-with-common-types-of-sqlalchemy-exceptions-for-running-sql-queries-in-python-9ec8db)
    - [Pydantic Error Handling](https://docs.pydantic.dev/latest/errors/errors/)

A complementary technique to exception handling is to log errors as well to help with debugging. This is not taught
until COMP0034 though you may want to investigate if you have time.