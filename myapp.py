from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import plotly.data as pldata

df = pldata.gapminder(return_type='pandas', datetimes=True)


# Initialize Dash app
app = Dash(__name__)
server = app.server

countries = df['country'].drop_duplicates()

# Layout
app.layout = html.Div([
    dcc.Dropdown(
        id="country-dropdown",
        options=[{"label": country_name, "value": country_name} for country_name in countries],
        value="Canada"
    ),
    dcc.Graph(id="gdp-growth")
])

# Callback for dynamic updates
@app.callback(
    Output("gdp-growth", "figure"),
    [Input("country-dropdown", "value")]
)
def update_graph(country):
    filtered = df[df['country'] == country]
    fig = px.line(filtered, x="year", y="gdpPercap", title=f"GDP per Capita Over Time: {country}")
    return fig

# Run the app
if __name__ == "__main__": 
    app.run(debug=True) 

    

