# 6. Using SQLModel to create an SQLite database

Classes that are defined with the argument `table=True` can be created in a database with a few lines of code.

```python
from sqlmodel import SQLModel, create_engine

# 1. Define the classes (code not shown here)

# 2. Create a connection to a SQLlite database, replace 'database_name.db' with path to the database and its name
engine = create_engine("sqlite:///database_name.db")

# 3. Create all the tables in the database
SQLModel.metadata.create_all(engine)
```

The following example is from the SQLModel documentation:

```python
from sqlmodel import Field, SQLModel, create_engine


class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: int | None = None


engine = create_engine("sqlite:///hero.db")

SQLModel.metadata.create_all(engine)
```

## Activity: Create the database

1. Make a copy of [starter_create_db_sqlmodel.py](../../src/activities/starter/starter_create_db_sqlmodel.py) which
   has classes to define the paralympics database consistent with
   what was created in week 3.
2. Add code to use the classes to create a database name `paralympics_sqlmodel.db` (you probably already have one called
   `paralympics.db`)

## Reflection on using copilot to generate the SQLModels from a sql schema

I generated the initial version of the SQLModel classes using copilot in Pycharm with paralympics_schema.sql attached
and the prompt: "Based on the .sql schema, write SQLModel classes"

The generated code was then checked against current SQLModel syntax:

- https://sqlmodel.tiangolo.com/tutorial/create-db-and-table/ to define a class (for a table)
- https://sqlmodel.tiangolo.com/tutorial/relationship-attributes/ for relationship attributes

Limitations of the initial copilot-generated solution:

- The attributes for date were treated as string. I decided to leave this since SQLite stores date as string
- Check constraints were not recognised. These are not directly supported in SQLModel in the current version.
  You need use SQLAlchemy syntax. This is not in the SQLModel documentation and the SQLAlchemy documentation is complex
  to follow. This article has a clear and shorter summary:
  https://plainenglish.io/blog/creating-table-constraints-with-sqlmodel

This table shows a solution for the check constraint:

```python
from typing import Optional

from sqlalchemy import CheckConstraint
from sqlmodel import Field, SQLModel


class Team(SQLModel, table=True):
    code: str = Field(primary_key=True)
    name: str
    region: Optional[str]
    sub_region: Optional[str]
    member_type: Optional[str]
    notes: Optional[str]
    country_id: Optional[int] = Field(default=None, foreign_key="country.id")

    __table_args__ = (
        CheckConstraint("member_type IN ('country', 'team', 'dissolved', 'construct')"),
        CheckConstraint("region IN ('Asia', 'Europe', 'Africa', 'America', 'Oceania')")
    )
```
- Foreign key constraints were also not recognised. This is a similar issue. To resolve it you need to define the field
  as a sqlalchemy.Column() with an argument for the constraint: 
```python
from sqlalchemy import Column, Integer, ForeignKey

sa_column=Column(
            Integer,
            ForeignKey("country.id", onupdate="CASCADE", ondelete="SET NULL"),
            nullable=True
        )
```

[Next activity](5-07-sqlmodel-add-data.md)