import pandas
from dash import Dash, html, dcc, callback, Input, Output
from plotly.express import line

file = "combined_output.csv"

data = pandas.read_csv(file)
data = data.sort_values(by="date")

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Pink Morsel Visualizer"),

    html.Div([
        html.Label("Select Region:"),
        dcc.RadioItems(
            id="region-filter",
            options=[
                {"label": " North", "value": "north"},
                {"label": " East", "value": "east"},
                {"label": " South", "value": "south"},
                {"label": " West", "value": "west"},
                {"label": " All Regions", "value": "all"}
            ],
            value="all",
            inline=True
        )
    ]),

    dcc.Graph(id="visualization")
], style={"padding": "20px", "fontFamily": "Arial, sans-serif"})

@callback(
    Output("visualization", "figure"),
    Input("region-filter", "value")
)
def update_chart(selected_region):
    if selected_region == "all":
        filtered_data = data
    else:
        filtered_data = data[data["region"] == selected_region]

    line_chart = line(
        filtered_data,
        x="date",
        y="sales",
        title=f"Pink Morsel Sales - {selected_region.capitalize()}"
    )

    return line_chart

app.run()
