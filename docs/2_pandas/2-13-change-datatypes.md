# Activity 2.10: Changing datatypes

The datatypes in the `events_csv_df` dataframe were output in activity 3; some columns have been removed leaving:

```text
type               object
year                int64
country            object
host               object
start              object
end                object
countries         float64
events            float64
sports              int64
participants_m    float64
participants_f    float64
participants      float64
```

Actions to be taken in this activity:

- Change 'float64' so the values display as '21' rather than '21.0'.
- The pandas reference states: "Columns with mixed types are stored with the object dtype". In this dataframe these are
  all strings, however the start and end should be dates.

The following summarises the data types needed in this activity. Note the differences for the integer types.
See [pandas reference](https://pandas.pydata.org/docs/reference/arrays.html) for other data types.

| Data Type       | Description                  | Typical Use Case                                                                       |
|:----------------|:-----------------------------|:---------------------------------------------------------------------------------------|
| float64         | Floating-point numbers       | Precise values, decimals                                                               |
| int64           | Large integers               | Whole numbers. 64-bit.                                                                 |
| Int64           | Large integers               | Whole numbers. 64.bit. Pandas-specific data-type that allows for missing numbers 'NaN' |
| int             | General integer type         | Usually same as int64. Size can vary.                                                  |
| DatetimeTZDtype | Timezone-aware datetime data | For timezone aware dates/times.                                                        |

A column's datatype can be specified when the data is read into a dataframe, e.g.

```python
import pandas as pd

# Define the data types for the columns
dtype_dict = {
    'column1': 'int',
    'column2': 'float64',
    'column3': 'int',
    # Add more columns as needed
}

# Read the CSV file with specified dtypes
df = pd.read_csv('your_file.csv', dtype=dtype_dict)
```

The datatype of a column can also be changed after the DataFrame is created, e.g.:

```python
# Convert a specific column from float64 to int
df['column_name'] = df['column_name'].astype('int')
```

## Activity: Change float64 to an integer type

1. Add code to your function to change all the float datatypes to integer (choose either int, int64, or Int64). The
   columns that need to be changed are
   `columns_to_change= ['countries', 'events', 'participants_m', 'participants_f', 'participants']`

Did you get an error? e.g.
`IntCastingNaNError(pandas.errors.IntCastingNaNError: Cannot convert non-finite values (NA or inf) to integer`.

Pandas cannot convert nulls, or NAs, to int. You will either need to remove, convert them, or convert to a type that
handles NaN ("Int64") e.g.

```python
df['col1'].fillna(0).astype(int)  # Replaces the missing values with 0
df['events'] = df['events'].astype('Int64')  # Handles NaN without replacing values
```

## Activity: Change object to date

The 'start' and 'end' columns contain dates as strings.

The pandas function `pd.to_datetime()`](https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html) can be
used to change strings to a datetime format.

See [Python datetime for the format codes](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes).

Use [pytz](https://pypi.org/project/pytz/) if you want to list all valid timezones.

1. Print the values from the 'start' and 'end' columns. You could use '.unique()' as in activity 8 or print the two
   columns.

   Are there any missing values? There shouldn't be.

2. Add code to change the date format `format='%d/%m/%Y'` using `pd.to_datetime()` e.g.
   `df['start'] = pd.to_datetime(df['start'], format='%d/%m/%Y')`. Optionally you can also make the dates timezone aware
   e.g. `df['start'] = df['start'].dt.tz_localize('Europe/London')`

3. Print the datatype of all columns again to see the difference after your changes. There are still some object data
   types. Try changing these to strings.

[Go to next activity](2-14-new-column.md)