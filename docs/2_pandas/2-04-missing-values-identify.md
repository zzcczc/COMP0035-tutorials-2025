# Activity 2.4: Identify missing values

Missing values or missing data are those values that are not present in the data set.

There are many reasons for values to be missing, for example because they don't exist, or because of improper data
collection or improper data entry.

Missing values in data can reduce the accuracy of any resulting data analysis or machine learning model.

In pandas, missing values are represented by None or NaN (**N**ot **a** **N**umber). Note that empty strings (`''`) are
not considered NA values.

In data science, missing values are typically categorised as:

- Missing Completely At Random (MCAR). There is no relationship between the missing data and any other vales in the
  dataset. There is no pattern for the missing values. The advantage of such data is that the statistical analysis
  remains unbiased.
- Missing At Random (MAR). The missing values are related to variables that are complete, i.e. there is a relationshp
  between the missing data and other values. The missing data may be estimated using the related values.
- Missing Not At Random (MNAR). There appears to be a pattern to the missing data; however this pattern does not depend
  on other variables that are in the dataset but some unknown variable. This can bias the results of any analysis.

[This article](https://www.analyticsvidhya.com/blog/2021/10/handling-missing-value/) summarises these succinctly.

## Activity: Find the missing values

You will need to refer to the pandas documentation:

- [dropna()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dropna.html)
- [fillna()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.fillna.html)
- [isnull()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.isnull.html)
- [isna()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.isna.html)

You could add the following to the describe function, or you could create a new function e.g. that explores the data, or
that checks data quality.

1. Add code that prints the number of missing values in the merged DataFrame using `isna()` or `isnull()`. 'True'
   indicates a
   missing value. Run the code to see the results.
2. Step 1 shows all the data which may not be practical in a large dataset. Instead, create a copy of the dataframe with
   only the rows that contain any missing values. Example of the syntax to create a DataFrame with missing
   rows: `missing_rows = original_df[original_df.isna().any(axis=1)]` or columns:
   `missing_columns = original_df[originial_df.isna().any(axis=0)]`.

[Next activity](2-05-plot-overview.md)