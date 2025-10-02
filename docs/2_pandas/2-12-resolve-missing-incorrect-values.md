# 12. Resolve missing or incorrect values

This activity addresses some of the data quality issues identified in the exploration stage:

- Missing values
- Mistakes in categorical values

## Missing values

There are different ways to deal with missing values. The decision you make will depend on the type of data, the actions
you want to perform on the data, and the reasons for the missing values.

Options include:

- **Do nothing**. It may be valid, e.g. the data does not yet exist so its absence is meaningful. It may not have
  significant impact on your analysis to ignore the missing values.
- **Delete**. If your data set is large enough you might choose to delete missing data without significant impact to the
  resulting analysis. Likewise, if the percentage of missing values is high, you may prefer to delete those rows
  or columns.
- **Fill (imputation)**. Use an imputation technique to fill the missing values e.g. mean, median, most frequent etc.

Imputation techniques are not covered in this course. This article
on [Towards Data Science](https://towardsdatascience.com/6-different-ways-to-compensate-for-missing-values-data-imputation-with-examples-6022d9ca0779)
gives pros and cons of some imputation techniques.

## Activity: Drop missing values

You identified the rows and columns with missing values in activity 4. You may want to repeat this now that you have
removed columns from the data.

There are missing values in the following rows/columns:

```text
       type  year country            host       start         end  countries  events  sports  participants_m  participants_f  participants  

0   Summer  1960   Italy            Rome  18/09/1960  25/09/1960       23.0   113.0       8             NaN             NaN         209.0  
17  summer  2028     USA     Los Angeles  15/08/2028  27/08/2028        NaN     NaN      22             NaN             NaN           NaN  
31  winter  2026   Italy  Milano Cortina  06/03/2026  15/03/2026        NaN    79.0       6             NaN             NaN           NaN 
```

Some pandas functions will function with `NaN` values; and some allow you to specify to ignore `NaN` using the parameter
`skipna=True`. Some functions, such as converting column data types, will fail if NaN are present, for these you need to
fill or remove NaN.

Write code to deal with the following:

1. The participants_m and participants_f data for Rome in 1960 is not available. Imputing the data would be inaccurate
   so remove row with index 0. To remove a row the syntax: `your_df_name = your_df_name.drop(index=0).
2. Numerous columns are missing from 17 and 31 as these are future events so the values are not known. Again, remove
   these rows as they aren't needed for the questions in this scenario.
3. Print the first 3 rows of the dataframe. You will see that row 0 is missing - pandas does not reset the index again
   from 0 unless you specify it should.
   e.g. `df = df.reset_index(drop=True)`

## Activity: Replace values

In activity 8 you found the following issues in the 'type' column:

```text
Distinct categorical values in the event 'type' column
 ['Summer' 'summer' 'winter ' 'winter']
```

Change `'Summer'` to `'summer'` and remove the trailing whitespace from `'winter '`.

1. Add code to locate the row where `type = "Summer"` using one of the approaches in activity 10. Once located, change
   it to lower case
   using ['.str.lower()'](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.lower.html#pandas.Series.str.lower)
   or set the value to 'summer'.

2. Add code to remove the whitespace from the 'winter ' occurrence by stripping whitespace either just from that cell,
   or from all values in the type column.
   Use ['.str.strip()'](https://pandas.pydata.org/pandas-docs/version/0.24/reference/api/pandas.Series.str.strip.html).

[Next activity](2-13-change-datatypes.md)
