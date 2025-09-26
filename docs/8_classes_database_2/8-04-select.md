# Activity 4: Select rows

In activity 3.14 the SQL select was introduced:

```sqlite
SELECT column_names
FROM table_name
WHERE some_condition
ORDER BY column_name -- ASC or DESC
LIMIT 1 -- or OFFSET
```

WHERE, ORDER BY and LIMIT/OFFSET are optional.

This activity introduces the SQLModel equivalent, [`select()`](https://sqlmodel.tiangolo.com/tutorial/select)

## Select (read) rows with SQLModel

As for the previous activities, you first create a Session(). This has been covered so is omitted here.

1. Create a `select` statement e.g. `statement = select(Games)`
2. Execute the statement and capture the results in a variable.

You can then use the results.

Often you want to select based on a condition using WHERE, e.g.: `WHERE name = 'Clare'`, `WHERE score > 25`, etc.

In SQLModel append `.where()` to `select()`: `select(Hero).where(Hero.name == "Dave")` NB: uses `==` **not** `=`

You can limit the number of results returned using LIMIT using `.limit()`, e.g.
`select(Hero).where(Hero.name == "Dave").limit(2)` to get the first 2 results.

Offset works the same way, so to skip the first 2 results: `select(Hero).offset(2)`

## Activity: select rows from the students database

Add code to select and print the results:

- select teacher where teacher_name == "Mark Taylor"
- select the names only for all the students

## Select with related tables

To select rows from tables that are related, you need to join the tables together.
 
SQL uses JOIN and specifies the common column between the tables to join on e.g.,

```sql
SELECT hero.id, hero.name, team.name
FROM hero
         JOIN team
              ON hero.team_id = team.id
```

When using join, consider how you want to join the tables. SQLite supports:

| Join type                                                       | Venn diagram                                    | Description                                                                                                                                                                                                                                                     |
|:----------------------------------------------------------------|:------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [INNER JOIN](https://www.sqlitetutorial.net/sqlite-inner-join/) | ![sql inner join](../img/sql-inner-join.png) | Selects all rows from both tables to appear in the result if and only if both tables meet the conditions specified in the ON clause.                                                                                                                            |
| [LEFT JOIN](https://www.sqlitetutorial.net/sqlite-left-join/)   | ![sql left join](../img/sql-left-join.png)   | Select results include:<br>Rows in table A (left table) that have corresponding rows in table B.<br>Rows in the table A table and the rows in the table B filled with NULL values in case the row from table A does not have any corresponding rows in table B. |
| [CROSS JOIN](https://www.sqlitetutorial.net/sqlite-cross-join/) |                                                 | Produces a Cartesian product of two tables; multiplying each row of the first table with all rows in the second table if no condition introduced with CROSS JOIN.                                                                                               |

RIGHT OUTER JOIN and FULL OUTER JOIN are not supported in SQLite.

SQLModel syntax varies depending on what result you want from the join. Some examples:

1. Select all Heros and their Teams: `statement = select(Hero, Team).where(Hero.team_id == Team.id)` gets the Hero and
   Team in the result for each Hero. Uses inner join.
2. Select all Heros and their Teams: `statement = select(Hero, Team).join(Team)` does the same as 1!
3. Select all Heros where they are in the team 'A':
   `statement = select(Hero).join(Team).where(Team.name == "Preventers")`. This is used where you want to find only the
   Hero attributes but based on a condition that is only in the associated table. Uses inner join.
4. Select all Heros and their Team even if they don't have a team (i.e. is null):
   `statement = select(Hero, Team).join(Team, isouter=True)` This is a LEFT OUTER JOIN.

You can join multiple tables together so long as there are keys that relate them. For example, find the Teachers who
teach Physics:

`select(Teacher.teacher_name).join(Enrollment).join(Course).where(Course.course_name == "Physics")`

## Activity: Select data from joined tables

Add code to select and print the results:

- Select all Students with their name and email that are enrolled on the Physics course, order by name descending
- Select all Courses that Student with id 1 is enrolled in

[Next activity](8-05-update.md)
