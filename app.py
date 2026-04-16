import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px

# load data
df = pd.read_csv("data/daily_sales_data_0.csv")

# simple graph
fig = px.line(df, x=df.columns[0], y=df.columns[1], title="Sales Trend")

# app
app = Dash(__name__)

app.layout = html.Div([
    html.H1("Sales Dashboard"),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run(debug=True)