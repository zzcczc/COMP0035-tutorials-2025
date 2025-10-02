# 7. Timeseries data

The previous activity considered the use of boxplots and histograms to visualise the distribution of the data.

This example uses a line chart. Line charts are useful for showing "patterns over
time". [Source: Depict](https://depictdatastudio.com/charts/line/). See
also [The Data Visualisation Catalogue](https://datavizcatalogue.com/methods/line_graph.html).

In a line plot, the x-axis usually represents the time, and the y-axis represents the variable(s) being measured.

The next charts consider the number of participants over time.

1. Create a new function to plot timeseries. Add code to create and show (or save)
   a [plot](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.html) where `x="start"`
   and `y="participants"`.

   Winter events have far fewer participants than summer, hence the effect you see in the chart.

If you wish to challenge yourself, display the charts showing the split of male and female participants.

You should be able to see from the charts that there appears to be an unusual dip in Winter 1994 Paralympics which may
need further investigation.

[Next activity](2-08-categorical-data.md)