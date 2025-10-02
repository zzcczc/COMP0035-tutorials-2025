# 4. Insert data into related tables

If you completed the exercise in week 3 to add data to the related tables you may remember the steps:

1. Add rows of data to the table with no relationships
2. Query to find the `id` of the parent row, then add the related child row in the other table using this `id` as the
   foreign key

The same approach is taken here to add the students, courses, teachers, locations and enrollments:

```python
def add_all_data():
    """Adds data from CSV to each table using pandas DataFrame to filter the data. """
    df = pd.read_csv(data_path)

    # Find the unique location rows then create Location objects from these
    locations = df["course_location"].unique()
    loc_objects = []
    for loc in locations:
        location = Location(room=loc)
        loc_objects.append(location)

    # Find the unique student rows then create Student objects from these
    rows = df.drop_duplicates(subset=['student_name'])
    stu_objects = []
    for _, row in rows.iterrows():
        student = Student(student_name=row["student_name"], student_email=row["student_email"])
        stu_objects.append(student)

    # Find the unique teacher rows then create Teacher objects from these
    # You may have already added teacher data, in which case exclude this section
    rows = df.drop_duplicates(subset=['teacher_name'])
    teacher_objects = []
    for _, row in rows.iterrows():
        teacher = Teacher(teacher_name=row.teacher_name, teacher_email=row.teacher_email)
        teacher_objects.append(teacher)

    # Find the unique coutse rows then create Course objects from these
    rows = df.drop_duplicates(subset=['course_name'])
    course_objects = []
    for _, row in rows.iterrows():
        course = Course(course_name=row.course_name, course_code=row.course_code, course_schedule=row.course_schedule)
        course_objects.append(course)

    with Session(engine) as session:
        # Add the objects to the individual tables. Note there are no primary or foreign key values at this stage.
        # Once the objects are added to the database, the primary key value will be created 
        session.add_all(loc_objects)
        session.add_all(stu_objects)
        session.add_all(teacher_objects)
        session.add_all(course_objects)
        session.commit()

        # Create and add the enrollment objects and add the location FK to the courses
        for _, row in df.iterrows():
            # Find the ids of the rows
            location = session.exec(select(Location).where(Location.room == row["course_location"])).first()
            s_id = session.exec(select(Student.id).where(Student.student_email == row["student_email"])).first()
            c_id = session.exec(select(Course.id).where(Course.course_code == row["course_code"])).first()
            t_id = session.exec(select(Teacher.id).where(Teacher.teacher_email == row["teacher_email"])).first()
            # Update the course with the location using the relationship attribute
            course.location = location
            # Create the new enrollment for the row
            enrollment = Enrollment(student_id=s_id, course_id=c_id, teacher_id=t_id)
            session.add_all([course, enrollment])
            session.commit()
```

Note that there are other ways to do the above, I used this approach as it is consistent with code you have seen in the
course to date.

## Activity: Add data to the database

1. Add a function to add all the data. You could add this to `app.py` as shown in the SQLModel tutorial. I created a new
   module `queries.py` instead for this and the following activities.

2. Use/adapt the code above to insert all the rows.

3. Run app.py to create the database and add the rows.

Note: If you run app.py repeatedly the rows will be appended to the tables. You could drop all the tables e.g., using
`SQLModel.metadata.drop_all(engine)`; or you could add queries to check if a table is empty before adding rows.

[Next activity](8-05-select.md)