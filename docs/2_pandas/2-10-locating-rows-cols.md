# Activity 10: Referencing specific columns and/or rows in a DataFrame

Many of the following activities work with specific columns and rows.

There are many ways to locate columns and rows in pandas. The following lists some of the more common you may see in
tutorials and examples online, there are other methods (mask, filter, ...).

- bracket notation to reference a column: `name_of_dataframe['col_name']`
- dot notation to reference a column: `name_of_dataframe.col_name` (works where there are no spaces or special
  characters in the column name)
- [`loc`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html) to identify a group of rows and
  columns using integer positions or column labels:
    - `name_of_dataframe.loc[7:9]` - row with index 7 and column with index
    - `name_of_dataframe[:, 'col_a']` - all rows from the column named 'col_a'
    - `name_of_dataframe[:, ['col_a','col_b]]` - all rows from columns named 'col_a' and 'col_b'
- [`iloc`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iloc.html#pandas-dataframe-iloc) to locate by
  integers only e.g.
    - `df.iloc[3]` row at index 3
    - `df.iloc[0, 1]` row 0, value from the second column (starts from 0)
    - `df.iloc[1:3, 0:3]` rows 1 and 2, and the first 3 columns
- [`iat`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iat.html#pandas-dataframe-iat) to Access a
  single value for a row/column pair by integer position e.g. `df.iat[1, 2]`
- [`at`]() get or set a value for a specific pair by integer or column label e.g. get `df.at[4, 'B']` or set
  `df.at[4, 'B'] = 10`
- [`query`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.query.html) used to query columns with an
  expression e.g. `df_summer = df.query("type == 'summer'")`. You can use expressions such as `==, !=, <, >, in`. You
  can use values of a variable e.g.
    ```python
    event_type = "winter"
    df_winter = df.query("type == @event_type")
    ```

You will need some these approaches in the following activities. Try to use different techniques so you explore
more features of pandas.

Here are some examples of how you could use the techniques above to find and then change a value:

```python
# Example 1: Find a row/column that matches a certain condition using loc with a query or mask
df.loc[df.query("type == 'Summer'").index, 'type'] = 'summer' # query
df.loc[df['type'] == 'Summer', 'type'] = 'summer' # mask

# Example 2: Find the index of the row using `query`, and then use `at` to update the value.
# NB Assumes only 1 row matches the criteria, amend to loop through all matching indices if more than one result.
index = df.query("type == 'Summer'").index[0]
df.at[index, 'type'] = 'summer'

# Example 3: Uses iloc which only works with integers so you need to find the row & column integer references first
row_pos = df.query("type == 'Summer'").index[0]
row_idx = df.index.get_loc(row_pos)
col_idx = df.columns.get_loc('type')
df.iloc[row_idx, col_idx] = 'summer'
```

[Next activity](2-11-removing-columns.md)