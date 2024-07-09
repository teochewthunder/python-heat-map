# Python Heatmap
This builds on the earlier [Python Bar Chart](https://github.com/teochewthunder/python-bar-chart). Differences are highlighted below.

## Data
- Same as Python Bar Chart.

## Script
- Generate a list of Seasons from the data.
- Generate a list of Players from the data. Iterate through `data`, adding player names to a list. After that, convert the list to a dictionary, which automatically removes all duplicates, then convert back to a list, and sort.
- Only request the user to enter 1 for Goals and 2 for Appearances.
  - Utilize a `Try-catch` to ensure only numerical data is entered.
  - If value is numerical but out of bounds, do-over.
  - If value is 0, end program.
- Use the selected stat to generate the two-dimensional list for the Heatmap.

## Chart
We use the `matplotlib` library to plot the heatmap, and the `numpy` library to access aggregation functions.
- "Reds" is passed into the method as the `cmap` argument, to turn the color scheme into a red-based palette.
- We use the `colorbar()` method to provide a legend.
- The `text()` method is used in a nested `For` loop that iterates through the data.
  - If the current value is less than the average of the dataset, use black as a color.
  - Otherwise, use white.
