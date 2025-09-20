# COMP0035 2025-26 Weekly practical activities

This repository contains the activities for the COMP0035 module for the academic year 2025-26.

## Instructions for using this repository

1. Fork this repository to your own GitHub account.
2. Clone the forked repository to your local machine (e.g. in VS Code or PyCharm).
3. Each week, update the repository using the 'Sync fork' button in GitHub to check for changes, if it is out of date
   then select the 'Update branch' button.

## Activity instructions and code files

The `docs` folder contains the activity instructions for each week.

The `src` package contains any starter code for each week. You can also use this package to store your own code
that you create during the activities.

One solution to the week's activities will be added to the [tutor_solution repository](). Other solutions will be
possible, and some may be better than the solution offered, so don't feel
your code has to match the tutors code!

## List of activity instructions

This will be updated each week with the activities for that week.

### Week 1 Source code control, environment, structure

Required:

1. [Python project structure](docs/1_structure/1-structure.md)
2. [Python virtual environment](docs/1_structure/2-environments.md)
3. [Source code control (GitHub)](docs/1_structure/3-source-code-control.md)
4. [Set up the course activities project and repository](docs/1_structure/4-activities-repo.md)
5. [Set up the coursework project and repository](docs/1_structure/5-coursework-repo.md)

Optional:

6. [Computer setup for COMP0035](docs/1_structure/6-opt-computer_setup.md)
7. [Integrate your IDE with GitHub](docs/1_structure/7-opt-integrate-IDE-GitHub.md)
8. [Using CoPilot in VS Code and PyCharm](docs/1_structure/8-opt-copilot-ide.md)

### Week 2 Pandas to describe, explore and prepare a dataset

This week's activities are more than you can complete in a week. There are less in week 4 so you could delay some to
that week.

1. [Create a package and module](docs/2_pandas/2-01-python-structure)
2. [Open .csv and .xlsx files and create a DataFrame](docs/2_pandas/2-02-pandas-df)
3. [Describe the dataframe](docs/2_pandas/2-03-pandas-describe)
4. [Identify missing values](docs/2_pandas/2-04-missing-values-identify.md)
5. [Overview of plots](docs/2_pandas/2-05-plot-overview.md)
6. [Plots to show distributions](docs/2_pandas/2-06-plot-distribution.md)
7. [Plots for timeseries data](docs/2_pandas/2-07-plot-timeseries.md)
8. [Columns with categorical values](docs/2_pandas/2-08-categorical-data)
9. [Data preparation](docs/2_pandas/2-09-data-prep.md)
10. [Locating rows and columns](docs/2_pandas/2-10-locating-rows-cols.md)
11. [Remove columns](docs/2_pandas/2-11-removing-columns.md)
12. [Remove and replace values](docs/2_pandas/2-12-resolve-missing-incorrect-values.md)
13. [Change data types](docs/2_pandas/2-13-change-datatypes.md)
14. [Add new data by computing](docs/2_pandas/2-14-new-column.md)
15. [Add new data by combining dataframes](docs/2_pandas/2-15-joining-dataframes.md)
16. [Save dataframe to file](docs/2_pandas/2-16-save-df-to-file.md)
17. [Check the prepared data suits the purpose](docs/2_pandas/2-17-questions.md)
18. [Next steps](docs/2_pandas/2-18-next-steps.md)

### Week 3 Database design; sqlite3

Activity instructions are in the docs/3_database folder, including:

1. [Introduction to database design (lecture recap)](docs/3_database/3-01-database-design.md)
2. [Introduction to ERD (lecture recap) and ERD drawing tools](docs/3_database/3-02-erd-intro.md)
3. [Conceptual database design](docs/3_database/3-03-conceptual-design.md)
4. [Logical design to 1NF](docs/3_database/3-04-logical-design-1nf.md)
5. [Logical design to 2NF](docs/3_database/3-05-logical-design-2nf.md)
6. [Logical design to 3NF](docs/3_database/3-06-logical-design-3nf.md)
7. [Logical design - constraints](docs/3_database/3-07-logical-design-constraints-data.md)
8. [Logical design - referential integrity](docs/3_database/3-08-logical-design-constraints-fk.md)
9. [Logical design activity](docs/3_database/3-09-logical-design-activity.md)
10. [Physical design - SQLite schema](docs/3_database/3-10-physical-design-structure.md)
11. [Phyical design - Python to create SQLite database structure](docs/3_database/3-11-physical-design-create-db.md)
12. [Database design - next steps](docs/3_database/3-12-next-steps.md)
    
The remaining activities are optional at this stage. They are not required in coursework 1.

13. [SQL INSERT and SELECT intro](docs/3_database/3-13-sql-add-data.md)
14. [Add data to tables with no FK](docs/3_database/3-14-insert-no-fk.md)
15. [Select data](docs/3_database/3-15-select-query.md)
16. [Add data to tables with an FK](docs/3_database/3-16-insert-with-fk.md) 
17. [Normalisation and application code](docs/3_database/3-17-normalisation-tradeoff.md)- A brief intro to the trade-off between database normalisation and query design

### Week 4 Code quality: linting, docstrings, PEP8/257, use of functions.

### Week 5 Database to Python class: ORM

### Week 6 Requirements; interface design

### Week 7 Application design

### Week 8 Classes; error handling

### Week 9 Unit testing, CI and coverage

### Week 10 No new activities

Tutorial reserved for final coursework support

## Data

Most activities use paralympics data that was compiled from
the [IPC website](https://www.paralympic.org/paralympic-games).

The data is duplicated in some instances in `src/data` and in `src/starter/resources`. This is for teaching purposes for
an activity that explains different methods to import the data in the project depending on its location within or
outside the package's directory structure.

### External examples using similar paralympics data

[Onyx data challenge 2024](https://zoomcharts.com/en/microsoft-power-bi-custom-visuals/challenges/onyx-data-september-2024?utm_source=youtube&utm_medium=social&utm_campaign=onyx_september24_workshop&utm_content=ZcHeader)