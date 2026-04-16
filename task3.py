import pandas
from dash import Dash, html, dcc
from plotly.express import line

file = "combined_output.csv"

data = pandas.read_csv(file)
data = data.sort_values(by="date")

app = Dash(__name__)

line_chart = line(data, x="date", y="sales", title="Pink Morsel Sales")
visualization = dcc.Graph(id="visualization", figure=line_chart)
header = html.H1("Pink Morsel Visualizer", id="header")

app.layout = html.Div([
    header,
    visualization
])

app.run()
