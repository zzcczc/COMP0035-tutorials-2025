# Activity 5: Update rows

To update one or more columns in a row the SQL syntax looks like this:

```sql
UPDATE hero
SET age=16
WHERE name = "Spider-Boy"
```

In SQLModel you select the row, or rows, as objects, update the attributes and commit the changes.

Example from the [SQLModel documentation](https://sqlmodel.tiangolo.com/tutorial/update):

```python
def update_heroes():
    with Session(engine) as session:
        statement = select(Hero).where(Hero.name == "Spider-Boy")
        results = session.exec(statement)
        hero = results.one()
        hero.age = 16
        session.add(hero)
        session.commit()
```

## Activity: Update students rows

Add code to update records, print the row before and after to check the results:

- update the course code for the Mathematics course to MATH102
- update all teacher email addresses with the new domain @newschool.com. For this you also need Python string .replace()
  `teacher_email.replace("@school.com", "@newschool.com")`

[Next activity](8-06-delete.md)