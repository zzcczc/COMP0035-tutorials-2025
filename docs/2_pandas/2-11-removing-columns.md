# 11. Removing columns

In the function to describe the events dataframe you printed all the column names:

```text
['type', 'year', 'country', 'host', 'start', 'end', 'disabilities_included', 'countries', 'events', 
    'sports', 'participants_m', 'participants_f', 'participants', 'highlights', 'URL']
```

You don't need the 'URL', 'disabilities_included' and 'highlights' columns in the scenario given. 

Options to remove columns:

1. Exclude the columns from the data file when the dataframe is created by specifying the columns to read
2. Removed the columns after the dataframe is created

## Create the database with specified columns

Use the `usecols` parameter when you read the data. For example:

```python
import pandas as pd
from pathlib import Path
from importlib import resources

from activities import data

if __name__ == '__main__':
    path_para_raw = resources.files(data).joinpath("paralympics_raw.csv")

    cols = ['type', 'year', 'country', 'host', 'start', 'end', 'countries', 'events', 'sports',
            'participants_m', 'participants_f', 'participants']

    df_selected_cols = pd.read_csv(path_para_raw, usecols=cols)
```

## Activity: Remove the columns after creating the dataframe

As you already have the columns in the dataframe, use this approach to remove them.

Use the [pandas.DataFrame.drop()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop.html) to remove
either rows or columns. To remove rows specify `axis=0`; to remove columns you can use `axis=1` or the `columns=`
parameter.

> `inplace=True` Most methods in pandas return a new object and leave the original untouched. To alter the DataFrame in-place you can
sometimes use the attribute `inplace=True`; though most examples suggest allocating the result of an action to a new
dataframe object as `inplace=True` can have unwanted implications in some
circumstances - [see here](https://docs.astral.sh/ruff/rules/pandas-use-of-inplace-argument/).

An example of allocating the result of an action to a new dataframe: `df_result = df.drop(columns=['MyCol2', 'MyCol4'])`

An example using `inplace=True` where the result will be accessed in the original `df`:
`df.drop(columns=['MyCol2', 'MyCol4'], inplace=True)`

1. Edit the function to drop the following list of named columns `['URL', 'disabilities_included', 'highlights']` and
   assign the result to a new DataFrame variable, e.g. `df_prepared`.
2. You might also want to add a print of the column names again so you can check the columns were removed. Run the code.

[Next activity](2-12-resolve-missing-incorrect-values.md)