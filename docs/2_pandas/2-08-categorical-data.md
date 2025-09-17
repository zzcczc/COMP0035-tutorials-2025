# Activity 2.8: Identifying values in categorical data

Categorical variables are those where the data can be divided into categories, or groups. For example: race, gender, age
group, and educational level.

Categorical variables can be problematic for data analysis.

One issue is that many machine learning algorithms cannot handle categorical data. To overcome this, categorical values
can be replaced with encoded data. For example: Hot = 1, Warm = 2, Cold = 3. Techniques for addressing this is not
covered in this course, however there are Python packages (or functions within packages) that will handle this process
of encoding; a popular option
is [OneHotEncoder](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwijhozWxe2BAxWaUkEAHegCDEYQFnoECB4QAQ&url=http%3A%2F%2Fscikit-learn.org%2Fstable%2Fmodules%2Fgenerated%2Fsklearn.preprocessing.OneHotEncoder.html&usg=AOvVaw0oQAupueEbfcv4c2Csd5dn&opi=89978449).

A second issue is that depending on how the data was collected, categorical data may be entered inconsistently, e.g. in
an address where the values "UK", "Great Britain", and "United Kingdon" all relate to the same country.
However, as they are spelt differently any functions to count, group etc. would not recognise the similarity.

The 'type' and 'disabilities_included' columns in the event data appear to have categorical data. You could also explore
the npc codes and medal standings data.

1. Write code to print unique values for the 'type' column. A single column is a Series so you can
   use [`df['ColName'].unique()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.unique.html) or [
   `df['ColName'].value_counts()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.value_counts.html).

   If you run the code you should see output something like this:

    ```text
    Distinct categorical values in the event 'type' column
     ['Summer' 'summer' 'winter ' 'winter']
    
    Count of each distinct categorical value in the event 'type' column
     type
    summer     17
    winter     13
    Summer      1
    winter      1
    Name: count, dtype: int64
    ```

   You can see there are two errors, winter has an extra space in on one row, and in another summer has a capital.

2. Repeat for the 'disabilities_included' column.

   The results here show a different issue; multiple values are included in a single cell. This will be addressed in a
   later week in database design.

[Next activity](2-09-resolve-issues.md)