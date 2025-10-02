# 15. Joining dataframes

In the medal_standings DataFrame there is a field called 'NPC' which contains the three-letter codes used by the
National Paralympic Committee (NPC) to describe a team. The teams are usually countries such as "China", or a construct,
such as "Neutral Para Athletes".

A list of all the current and historic NPC codes is the data file `activities/data/npc_codes.csv` (the Excel version
has the same data).

You don't really need this to answer the questions the scenario; though it may be useful in later analysis to indicate
the NPC code for each of the paralympic events. This activity looks at how you can join data from one dataframe to
another.

To join the data from two dataframes, there needs to be a column that is common to both. In this case:

- `npc_codes.csv` : "Name"
- `paralympics_events` : "country"

"Name" and "country" both appear to contain the country name.

There are two Pandas functions for combining data:

- To combine two dataframes with a common index or key column (i.e. a column with unique values only) you can
  use [pandas.DataFrame.join()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.join.html?highlight=join#pandas.DataFrame.join)
- To combine two dataframes where the common column is not an index or key then you
  use [pandas.DataFrame.merge()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.merge.html?highlight=merge#pandas.DataFrame.merge)

In this case 'merge' is needed as the values in country are not unique in the events csv.

There are different approaches to combine data. These are:

- **left**: use calling frame’s index (or column if on is specified)
- **right**: use other's index.
- **outer**: form a union of calling frame's index (or column if on is specified) with other's index, and sort it
  lexicographically.
- **inner**: form intersection of calling frame's index (or column if on is specified) with other's index, preserving
  the
  order of the calling’s one.
- **cross**: creates the cartesian product from both frames, preserves the order of the left keys.

Start with the 'events' dataframe which is the one you want to add the 'NPC' column to. This has ~30 rows. This is the
**left**dataframe.

The **right** dataframe is the npc_codes. This has ~130 rows.

Using the different methods to combine the data:

- left: the resulting dataframe would add the NPC code to the 'events'. The result will be ~30 rows.
- right: the resulting DataFrame will have ~130 rows (same as the 'npc_codes' DataFrame). This is because a right join
  includes all rows from the right DataFrame and matches rows from the left DataFrame based on the join key. If there
  are no matching rows in the left DataFrame, the result will contain NaN for those columns.
- outer: the resulting DataFrame will include all unique rows from both DataFrames. This means it forms the union of the
  columns ('Name', 'country') from both DataFrames. The exact number of rows in the resulting DataFrame depends on the
  overlap between the columns of the two DataFrames.
- inner: the resulting DataFrame will only include rows that have matching columns in both DataFrames. The number of
  rows in the resulting DataFrame depends on the overlap between the columns of the two DataFrames. If there is no
  overlap, the resulting DataFrame will have 0 rows. If there is complete overlap, the resulting DataFrame will have the
  same number of rows as the smaller DataFrame.
- cross: if the left DataFrame has 32 rows and the right DataFrame has 132 rows, the resulting DataFrame will have: ~
  30 * 130 = 4000+ rows.

Use the 'left' method for this activity.

The available parameters in the merge function are:
`DataFrame.merge(right, how='inner', on=None, left_on=None, right_on=None, left_index=False, right_index=False, sort=False, suffixes=('_x', '_y'), copy=None, indicator=False, validate=None)`

You need to specify the following:

`left_dataframe_name.merge(right_dataframe name, how='left', left_on='col_name_in_left_df', right_on='col_name_in_right_df')`


1. Open the npc_codes.csv into a DataFrame, reading in just the 'Name' and the 'Code' columns as we only need these.
   The parameter `usecols=['Code', 'Name']` for the pd.read_csv function is useful here.

   Note: there is a problematic character somewhere in the npc_codes.csv file. You can read the file using the
   additional parameters from this example:
   `df = pd.read_csv(path_to_npc_csv_file, encoding='utf-8', encoding_errors='ignore', usecols=['col1', 'col2'])`
2. Add the code to 'merge' the two dataframes and create a new merged dataframe with the result.
3. Print the 'country', 'Code', 'Name' columns from the merged dataframe.

    This is just the rows with NaNs:
    
    ```text
        country Code Name
    6       UK  NaN  NaN
    7    Korea  NaN  NaN
    9      USA  NaN  NaN
    12   China  NaN  NaN
    13      UK  NaN  NaN
    17     USA  NaN  NaN
    25     USA  NaN  NaN
    28  Russia  NaN  NaN
    29   Korea  NaN  NaN
    30   China  NaN  NaN
    ```
    
    There are numerous 'NaN's. Why?
    
    To match the values in the columns 'country' and 'Name' needed to be identical. Unfortunately, countries often have
    different ways being written in English, so for example UK in the events data, and United Kingdom in the NPC data.
    
    Dealing with NaNs and Nulls is covered in activity 12.

4. The values that are NaN are the country codes for UK, USA, Korea, Russia and China. In the NPC file these are:

    ```python
    replacement_names = {
        'UK': 'Great Britain',
        'USA': 'United States of America',
        'Korea': 'Republic of Korea',
        'Russia': 'Russian Federation',
        'China': "People's Republic of China"
    }
    ```

   Add code _before_ the code to merge the two dataframes. The code should change the values in the `['country']` column
   to those in the dict given above.

   Use
   the [Series.replace(to_replace=replacement_names) function](https://pandas.pydata.org/docs/reference/api/pandas.Series.replace.html#pandas.Series.replace).
5. Check for NaNs again too check all have been addressed.
6. Remove the 'Name' column as it is a duplicate of the 'country' column
7. Optionally print the dataframe contents to check the results are what you expected.

[Next activity](2-16-save-df-to-file.md)