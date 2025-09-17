# Activity 2.9: Data preparation

The following activities move on from describing the dataframe and exploring its contents, to changing its contents to
suit our purposes. These activities are often referred to as 'data preparation' or 'data cleaning'.

In this activity you will prepare the data so that it can be used for a particular purpose.

You are asked to prepare the data for use in a dashboard web application for high school students (the 'target
audience'). The questions the students are interested in are:

- where in the world have paralympic events have been held?
- when have the events been held? (dates)
- how have the number of sports and events included changed over time?
- what are the trends in participant numbers over time? How does this vary by gender? How does this vary by winter and
  summer events?

In the activities you are guided to create one dataframe that can be used for any of these questions for simplicity; you
could choose to prepare the data separately for each question.

In doing so you will also address the issues that were identified during the exploration activities:

- remove columns that are not needed
- resolve issues with missing values
- change data types
- correct categorical data
- add new data: new columns, merge datasets

The following activities focus on the paralympic games data and the country codes, rather than the medal standings. You
can use the medal standings data for extra practice.

## Activity: Create a new function

The function should take a DataFrame of the raw paralympics event data, perform actions to prepare it for your needs,
and then return a dataframe with the prepared data and/or save the data to a .csv or .xlsx file.

You can choose whether the function just deals with all the changes for the data preparation, or whether to have
separate smaller functions for each.

Create the outline of the function. You can create it in a new module, or use your existing one.

[Next activity](2-11-removing-columns.md)