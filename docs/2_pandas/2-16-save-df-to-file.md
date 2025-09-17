# Activity 2.16: Save the prepared dataset

You have now carried out the data cleaning and preparation steps needed for this project so save the prepared
dataframe back to a .csv file.

You could also save the data to a database or other format.
See [pandas output methods](https://pandas.pydata.org/docs/reference/io.html#).

1. Add code add the end of the data preparation function to save the output to file in the 'data' directory before you
   return the dataframe. You could remove the return dataframe from the end of the function if you prefer. Use the
   pandas ['to_csv()'](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html).

   Note that the dataframe has an index column with row numbers that you don't need in the csv file. Use the
   argument `index=False` when you use `to.csv()`

2. Finally, add code to return the dataframe from the function so it can be used by other functions e.g. `return df`

3. Run the code and check that the file is saved.

[Next activity](2-17-questions.md)