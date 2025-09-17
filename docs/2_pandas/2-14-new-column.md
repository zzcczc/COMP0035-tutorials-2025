# Activity 2.9: Adding new columns

The next two activities add data to the existing data:

- Add a new column by computing a value
- Add a new column by merging data from another dataframe

Adding new data may introduce new issues with NaN, incorrect values, incorrect formats etc. so you would need to repeat
many of the previous steps! The new data could have been added before we did the rest of the preparation.

## Activity: Add computed values

One way to add new data is to compute new values from the existing data.

Add a new column called `duration` with its values calculated by subtracting the start date from the end date. This
should work as you converted the strings to date data types in the last activity.

This uses the [`DataFrame.insert()` function](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.insert.html#pandas.DataFrame.insert).

1. The code to calculate the new column could be written as:  `df['duration'] = df['end'] - df['start']`. This would
   append the column to be the last in the DataFrame with a date datatype expressed in days e.g. '4 days'
2. Instead, add code first calculate the values as an integer format:
   `duration_values = (df['end'] - df['start']).dt.days.astype('Int64')`
3. Then insert the values as a new column the 'end' column using the `DataFrame.insert()` function e.g.
   `df.insert(df.columns.get_loc('end') + 1, 'duration', duration_values)`
    - `df.columns.get_loc('end')`: Finds the index of the 'end' column and adds 1 to set the position of duration after the end column. 
    - `'duration'`: The name of the new column.
    - `duration_values`: The values for the new column.
4. Run the code. You could `print(df['duration'])` to check the result.

[Next activity](2-15-joining-dataframes.md)