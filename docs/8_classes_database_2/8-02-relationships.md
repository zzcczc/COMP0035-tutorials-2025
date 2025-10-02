# 2. Relationships in SQLModel

## One-to-many

You already know that to achieve this you add the primary key attribute from the parent table as a foreign key
attribute to the child table.

To do this in SQLModel you define the foreign key field like this example from the SQLModel documentation:

```python
from sqlmodel import Field, Session, SQLModel


class Team(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    headquarters: str


class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    secret_name: str
    age: int | None = Field(default=None, index=True)

    team_id: int | None = Field(default=None, foreign_key="team.id")
```

SQLModel (and SQLAlchemy) has an advantage over pure SQL as it allows you to navigate the relationship from both child
to parent AND parent to child by defining a `Relationship()` attribute in both classes.

This is the updated example from the SQLModel documentation:

```python
from sqlmodel import Field, Relationship, SQLModel


class Team(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    headquarters: str

    heroes: list["Hero"] = Relationship(back_populates="team")


class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    secret_name: str
    age: int | None = Field(default=None, index=True)

    team_id: int | None = Field(default=None, foreign_key="team.id")
    team: Team | None = Relationship(back_populates="heroes")
```

Notice that "Hero" has quote marks in `heroes: list["Hero"] = Relationship(back_populates="team")`. This is because Hero
is defined after Team, so you would get an error warning in your IDE if you try to enter it as `list[Hero]`. Adding the
`""` makes the interpreter see it as a string. More on
this [here](https://sqlmodel.tiangolo.com/tutorial/relationship-attributes/type-annotation-strings/#about-the-string-in-listhero).

When you have a relationship defined in this way, and you append an object to the List attribute, then when you add and
commit, SQLModel makes sure that the changes to both tables are made.
See [SQLMOdel documentation](https://sqlmodel.tiangolo.com/tutorial/relationship-attributes/create-and-update-relationships/#include-relationship-objects-in-the-many-side).

### Cascade delete/update

Updates are handled using the `back_populates` argument in the Relationship.

Cascade delete constraints on the relationships require more knowledge to implement in SQLModel. This is sign-posed for
students who want
to [read further](https://sqlmodel.tiangolo.com/tutorial/relationship-attributes/cascade-delete-relationships/); but not
covered in the course activities.

## Many to many

As you saw in the normalisation activity in week 3, many-to-many relationships are resolved by creating a new table
between the tables to join or link them.

The `Relationship()` can still be defined on the two tables that have the many-to-many, note the extra parameter
`link_model`.

The example from the SQLModel documentation:

```python
from sqlmodel import Field, Relationship, SQLModel


class HeroTeamLink(SQLModel, table=True):
    team_id: int | None = Field(default=None, foreign_key="team.id", primary_key=True)
    hero_id: int | None = Field(default=None, foreign_key="hero.id", primary_key=True)


class Team(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    headquarters: str

    heroes: list["Hero"] = Relationship(back_populates="teams", link_model=HeroTeamLink)


class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    secret_name: str
    age: int | None = Field(default=None, index=True)

    teams: list[Team] = Relationship(back_populates="heroes", link_model=HeroTeamLink)
```

### Activity: Review the relationships for the student database

1. Open [models.py](../../src/activities/starter/db_wk8/models.py)
2. Find the example of a one-to-many relationship between course and location
3. Find the example of a many-to-many relationship between course, teacher and student in the enrollment table - this
   has a 3-way link table!

[Next activity](8-03-insert.md)