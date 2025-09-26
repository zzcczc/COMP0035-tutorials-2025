# 3. Insert data into related tables

If you completed the exercise in week 3 to add data to the related tables you may remember the steps:

- add table to the table with no relationships
- query to find the `id` of the related row, then add the row to the other table

When using an ORM such as SQLModel or SQLAlchemy, you use the relationship attributes to find the related records.

Since Enrollment has relationships called teacher, student and course, then by creating a teacher (t), a student (s) and
a course (c) and passing these to enrollment (e) then to save all the associated rows with related ids you might only
need to add the enrollmemt (e).

Iterating through the dataframe to append the values to a list and using `session.add_all()` will be more efficient
than adding each separately.

In principle the following code should suffice:

```python
def add_all_data():
    data_path = resources.files(data).joinpath("student_data.csv")
    df = pd.read_csv(data_path)
    enrollments = []
    for _, row in df.iterrows():
        values = row.to_dict()
        t = Teacher(**values)
        s = Student(**values)
        c = Course(**values)
        e = Enrollment(teacher=t, student=s, course=c)
        enrollments.append(e)
    with Session(engine) as session:
        session.add_all(enrollments)
        session.commit()
```

However, if you run the code above you will find duplicates for the Teacher, Student and Course as these are repeated in
the rows.

We need to add these only if they don't already exist so the code is a little more complex:

```python
def add_data_without_duplicates():
    """ Adds data without duplicates from the database."""
    data_path = resources.files(data).joinpath("student_data.csv")
    df = pd.read_csv(str(data_path))

    teachers = {}
    students = {}
    courses = {}
    enrollments = []

    for _, row in df.iterrows():
        values = row.to_dict()

        teacher_key = values["teacher_email"]
        student_key = values["student_email"]
        course_key = values["course_code"]

        # Only add the teacher, student and course if they have not already been added
        if teacher_key not in teachers:
            teachers[teacher_key] = Teacher(**{k: values[k] for k in ["teacher_name", "teacher_email"]})
        if student_key not in students:
            students[student_key] = Student(
                **{k: values[k] for k in ["student_name", "student_email"]})
        if course_key not in courses:
            courses[course_key] = Course(**{k: values[k] for k in ["course_code", "course_name"]})

        t = teachers[teacher_key]
        s = students[student_key]
        c = courses[course_key]
        e = Enrollment(teacher=t, student=s, course=c)
        enrollments.append(e)

    with Session(engine) as session:
        session.add_all(teachers.values())
        session.add_all(students.values())
        session.add_all(courses.values())
        session.add_all(enrollments)
        session.commit()
```

## Add data to the database

1. Add a function to add all the data. You could add this to `app.py` as shown in the SQLModel tutorial. I created a new
   module `queries.py` instead for this and the following activities.

2. Use/adapt the code above to insert all the rows.

3. Run app.py to create the database and add the rows.

Note: If you run app.py repeatedly the rows will be appended to the tables. You could drop all the tables e.g., using
`SQLModel.metadata.drop_all(engine)`.