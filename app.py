import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px

df = pd.read_csv("cleaned_data.csv")
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

df_grouped = df.groupby("date", as_index=False)["sales"].sum()

fig = px.line(
    df_grouped,
    x="date",
    y="sales",
    title="Pink Morsel Sales Over Time",
    labels={"date": "Date", "sales": "Sales"}
)

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Pink Morsel Sales Visualiser"),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run(debug=True)