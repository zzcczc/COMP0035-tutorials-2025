""" SQLModel classes for the students database. """
from typing import Optional

from sqlmodel import Field, Relationship, SQLModel


class Student(SQLModel, table=True):
    student_id: Optional[int] = Field(default=None, primary_key=True)
    student_name: str
    student_email: str = Field(unique=True)

    enrollments: list["Enrollment"] = Relationship(back_populates="student", cascade_delete=True)


class Teacher(SQLModel, table=True):
    teacher_id: int | None = Field(default=None, primary_key=True)
    teacher_name: str
    teacher_email: str = Field(unique=True)

    enrollments: list["Enrollment"] = Relationship(back_populates="teacher", cascade_delete=True)


class Course(SQLModel, table=True):
    course_id: int | None = Field(default=None, primary_key=True)
    course_name: str
    course_code: int = Field(default=None, primary_key=True)
    course_schedule: str | None = None
    course_location: str | None = None

    enrollments: list["Enrollment"] = Relationship(back_populates="course", cascade_delete=True)


class Enrollment(SQLModel, table=True):
    student_id: int | None = Field(foreign_key="student.student_id", primary_key=True, ondelete="CASCADE")
    course_id: int | None = Field(foreign_key="course.course_id", primary_key=True, ondelete="CASCADE")
    teacher_id: int | None = Field(foreign_key="teacher.teacher_id", primary_key=True, nullable=True,
                                      ondelete="SET NULL")
    teacher: Optional[Teacher] = Relationship(back_populates="enrollments")
    course: Optional[Course] = Relationship(back_populates="enrollments")
    student: Optional[Student] = Relationship(back_populates="enrollments")

