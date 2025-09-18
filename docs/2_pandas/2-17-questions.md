# Activity 2.17: Using the prepared data

The purpose of this activity to see whether it looks like the prepared data would suit the purposes.

## Recap of the purpose of the data

You were asked to prepare the data for use in a dashboard web application for high school students (the 'target
audience').

The questions the students are interested in are:

- where in the world have paralympic events have been held?
- when have the events been held? (dates)
- how have the number of sports and events included changed over time?
- what are the trends in participant numbers over time? How does this vary by gender? How does this vary by winter and
  summer events?

This activity is not concerned with answering the questions and interpreting the data; only in confirming if the data
preparation is sufficient. Charts are created a visual means of judging if the prepared data appears to be sufficient
for use in the intended scenario. You may identify other ways than charts to validate this.

You can create another function for this, or add the code to main.

## Where in the world have paralympic events have been held?

The data set contains city locations and the country of that city.

1. Add code to print the unique host-country pairs in which the games have been hosted. You could just print the two
   columns, or try `pairs = df[['host', 'country']]` and apply the `drop_duplicates()` and `sort_values(by='country')`
   functions. You can chain these functions together.

Is the prepared data sufficient? This is subjective. The NPC data also had region which might also be added to allow
someone to
answer. If you wanted to map the locations you would need to find the latitude and longitude of the host cities as well.

## When have the events been held?

You could do this by printing the values, or by displaying on a timeline. The following guides you through creating a timeline.




## How have the number of sports and events included changed over time?

Over to you, have a go at demonstrating you have the data to allow someone to answer the remaining questions:

- What are the trends in participant numbers over time?
    - How does this vary by gender?
    - How does this vary by winter and summer events?

[Next activity](2-18-next-steps.md)