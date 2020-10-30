import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('../data/mpg.csv')

data = [go.Scatter(          # start with a normal scatter plot
    x=df['acceleration'],
    y=df['horsepower'],
    text=df['name'],
    mode='markers',
    marker=dict(size=df['weight']/150) # set the marker size
)]

layout = go.Layout(
    xaxis = dict(title = 'acceleration'), # x-axis label
    yaxis = dict(title = 'horsepower'),        # y-axis label
    hovermode='closest'
)
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig)
