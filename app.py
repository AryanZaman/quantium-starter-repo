import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

# load cleaned data
df = pd.read_csv("cleaned_data.csv")
df["date"] = pd.to_datetime(df["date"])

app = Dash(__name__)

app.layout = html.Div(
    style={"fontFamily": "Arial", "padding": "20px"},
    children=[

        html.H1(
            "Pink Morsel Sales Dashboard",
            style={"textAlign": "center", "color": "#2c3e50"}
        ),

        html.Div(
            [
                html.Label("Select Region:", style={"fontWeight": "bold"}),

                dcc.RadioItems(
                    id="region-filter",
                    options=[
                        {"label": "All", "value": "all"},
                        {"label": "North", "value": "north"},
                        {"label": "East", "value": "east"},
                        {"label": "South", "value": "south"},
                        {"label": "West", "value": "west"},
                    ],
                    value="all",
                    inline=True
                ),
            ],
            style={"marginBottom": "20px"}
        ),

        dcc.Graph(id="sales-graph")
    ]
)

# callback to update graph
@app.callback(
    Output("sales-graph", "figure"),
    Input("region-filter", "value")
)
def update_graph(selected_region):

    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["region"] == selected_region]

    # group by date
    df_grouped = filtered_df.groupby("date", as_index=False)["sales"].sum()

    fig = px.line(
        df_grouped,
        x="date",
        y="sales",
        title="Sales Over Time",
        labels={"date": "Date", "sales": "Total Sales"}
    )

    return fig


if __name__ == "__main__":
    app.run(debug=True)