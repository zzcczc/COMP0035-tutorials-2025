# Activity 2.3: Use pandas to describe the contents of a DataFrame

In this activity you will use some of the pandas functions to describe the contents of the DataFrames:

- [DataFrame.shape](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.shape.html) - Returns the number of
  rows and columns in the DataFrame
- [DataFrame.head](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.head.html)
  and [DataFrame.tail](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.tail.html) - Returns the first /
  last 5 rows of the dataframe
- [DataFrame.columns](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.columns.html) - Returns the column
  labels
- [DataFrame.dtypes](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dtypes.html) - Returns the data types
  in the columns of the dataframe. Columns with mixed types are stored with the object dtype.
- [DataFrame.info](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.info.html) - Prints information about a
  DataFrame including the index dtype and columns, non-null values and memory usage.
- [DataFrame.describe](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html) - descriptive
  statistics include those that summarize the central tendency, dispersion and shape of a dataset’s distribution

## Activity: Create a function stub and docstring

Write the code in a way that makes it potentially re-usable in an application. This is expected for the coursework.

1. Import`pandas` which by convention is imported using the syntax `import pandas as pd`.
2. Create the structure for a Python function in the module. This function will take a DataFrame as its
   argument. It will print information that describes the data in the DataFrame.
3. Add a docstring to the function. The following is a general format for a multi-line docstring; specific
   styles include [Google](https://github.com/google/styleguide/blob/gh-pages/pyguide.md#38-comments-and-docstrings),
   reStructuredText (reST), Numpydoc, Epytext, and more. If you are using Co-pilot inline chat try
   `/doc format as Google-style docstring` or similar. Docstring example:
   ```python
   def some_function(argument1):
        """Summary or description of the function
    
           Parameters:
           argument1 (int): Description of argument1
    
           Returns:
           int: Description of the returning value
    
        """
    ```

NB This is not the only way to structure the code. For example, you could define the function differently, or use a class.

## Activity: add pandas functions to describe the dataset

1. Add to the function code that does the following:
    - Print the shape e.g. `print(name_of_your_dataframe.shape)` to find the number of rows and columns
    - Print the first 5 rows and the last 5 rows (you may need to change the Pandas settings to see all columns by using
      `pd.set_option("display.max_columns", None)`)
    - Print the column labels
    - Print the column datatypes
    - Print the info
    - Print the results of `describe`

2. Add code to your 'main' to call it for each of the three dataframes. It may look something like this, though you may
   have different names for your variables and functions:

    ```python
    if __name__ == "__main__":
        # Filepath of the csv data file (you may have used importlib.resources rather than pathlib.Path)
        paralympics_csv = Path(__file__).parent.parent.joinpath("data", "paralympics_raw.csv")
    
        # Read the data from the file into a Pandas dataframe
        events_csv_df = pd.read_csv(paralympics_csv)
       
        # Call the function named 'describe_dataframe' - you may have a different name for your function
        describe_dataframe(events_csv_df)
    ```

3. Run your Python code and look at the output to check you understand the results. The resulting printed information
   for the two dataframes with the 'events' data should be the same, the 'medal_standings' dataframe info will be
   different.

[Next activity](2-04-missing-values-identify.md)