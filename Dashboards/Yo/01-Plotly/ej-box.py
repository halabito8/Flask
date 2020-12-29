#######
# Objective: Make a DataFrame using the Abalone dataset (../data/abalone.csv).
# Take two independent random samples of different sizes from the 'rings' field.
# HINT: np.random.choice(df['rings'],10,replace=False) takes 10 random values
# Use box plots to show that the samples do derive from the same population.
######

# Perform imports here:
import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd




# create a DataFrame from the .csv file:
df = pd.read_csv('../data/abalone.csv')

# take two random samples of different sizes:
rand1 = np.random.choice(df['rings'],10,replace=False)
rand2 = np.random.choice(df['rings'],10,replace=False)

# create a data variable with two Box plots:

data = [
    go.Box(
        y=rand1,
        name='Rings 1'
    ),
    go.Box(
        y=rand2,
        name='Rings 2'
    )
]

# add a layout


# create a fig from data & layout, and plot the fig
fig = go.Figure(data=data)
pyo.plot(fig)
