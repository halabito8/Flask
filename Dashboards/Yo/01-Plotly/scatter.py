import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

np.random.seed(42)

randx = np.random.randint(1,101,100)
randy = np.random.randint(1,101,100)

data = [go.Scatter(x=randx,
                   y=randy,
                   mode='markers',
                   marker=dict(
                       size=10,
                       color='rgb(30,200,45)',
                       symbol='diamond',
                       line={'width':2}
                   ))]

layout = go.Layout(title='A si bueno',
                   xaxis={'title': 'Esto es X'},
                   yaxis={'title': 'Y esto y'},
                   hovermode='closest')

fig = go.Figure(data=data,layout=layout)

pyo.plot(fig, filename='scatter.html')