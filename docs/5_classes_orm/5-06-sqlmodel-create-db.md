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

## Adding data

To add a single record to a database table is conceptually similar to the code used with sqlite: create the instance,
add it, commit it.

```python
hero_1 = Hero(name="Deadpond", secret_name="Dive Wilson")
hero_2 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")

engine = create_engine("sqlite:///database.db")

with Session(engine) as session:
    session.add(hero_1)
    session.add(hero_2)
    session.commit()
```

To add data to the database, you can read the values into classes and create object instances. There are many ways you
could do this. Since you already have code to read from .xslx into a pandas DataFrame, use that. The code would be
structured something like this:

```python
import pandas as pd
from sqlmodel import Session, SQLModel, create_engine
from mymodels import MyData  # Replace with your actual model

# 1. Read Excel file
df = pd.read_excel("your_data.xlsx")

# 2. Convert DataFrame rows to SQLModel instances
records = [MyData(**row.to_dict()) for _, row in df.iterrows()]

# 3. Insert into database
engine = create_engine("sqlite:///mydatabase.db")
with Session(engine) as session:
    session.add_all(records)
    session.commit()
```

## Activity: Add data to the new paralympics database

Adding data to the paralympics database is more complex than the example above due to the number of tables so the code
has been written for you in .

Have a look at the code and then run it to add the data. You may need to edit the code to match the name and location of
the database to your structure.

[Next activity](5-07-summary.md)