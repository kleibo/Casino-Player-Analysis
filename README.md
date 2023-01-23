# Casino-Player-Analysis

## Linear Regression

The program first runs a linear regression on each individual player's data, creating a separate model for each player. The user can then select a player from a dropdown list to view the linear regression plot for that player. The plot displays the total theo on the y-axis and gaming date on the x-axis.


## K-Means Clustering

The program then uses k-means clustering to group players into four clusters: high frequency/high theo players, high frequency/low theo players, low frequency/high theo players, and low frequency/low theo players. The user can view a scatter plot of the players and their clusters, with the x-axis being total visits and the y-axis being total theo.


## Dependencies

This program uses the following libraries:
    -pandas
    -scikit-learn
    -matplotlib
    -tkinter

## Usage

To run the program, use the following command in the terminal:
``` python
python main.py
```

The program will open a file dialog for the user to select the player data file. Once selected, the user will have the option to select which analysis to run.
