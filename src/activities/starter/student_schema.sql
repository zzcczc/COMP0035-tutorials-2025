-- Schema for the student records database
PRAGMA foreign_keys = ON;
CREATE TABLE student
(
    student_id    INTEGER PRIMARY KEY,
    student_name  TEXT NOT NULL,
    student_email TEXT NOT NULL UNIQUE
);
CREATE TABLE teacher
(
    teacher_id    INTEGER PRIMARY KEY,
    teacher_name  TEXT NOT NULL,
    teacher_email TEXT NOT NULL UNIQUE
);
CREATE TABLE course
(
    course_id       INTEGER PRIMARY KEY,
    course_name     TEXT    NOT NULL,
    course_code     INTEGER NOT NULL,
    course_schedule TEXT,
    course_location TEXT
);
CREATE TABLE enrollment
(
    student_id INTEGER NOT NULL,
    course_id  INTEGER NOT NULL,
    teacher_id INTEGER,
    PRIMARY KEY (student_id, course_id, teacher_id),
    FOREIGN KEY (student_id) REFERENCES student (student_id) ON DELETE cascade ON UPDATE cascade,
    FOREIGN KEY (course_id) REFERENCES course (course_id) ON DELETE cascade ON UPDATE cascade,
    FOREIGN KEY (teacher_id) REFERENCES teacher (teacher_id) ON UPDATE cascade ON DELETE SET NULL
);