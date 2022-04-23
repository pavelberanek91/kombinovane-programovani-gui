from dash import Dash
from dash import dcc
from dash import html
from dash import Output         
from dash import Input          
import plotly.express as px
import pandas as pd

df = pd.read_csv("life_expectancy.csv")

#pridani externiho styloveho sesitu do aplikace
app = Dash( 
    __name__, #external_stylesheets="https://codepen.io/loremipsum/style.css",
)

#alternativni zpusob pridani sesitu
#app.css.append_css({"external_url": "https://codepen.io/loremipsum/style.css"})

#data pro inline stylovani prvku
colors = {"background": "#011833", "text": "#7FDBFF"}

app.layout = html.Div([

        #inline stylovani prvku (test funkcnosti)
        html.H1("Dashboard", style={"color": "red"}),

        #vyuzivani trid z lokalniho styloveho souboru v souboru ve slozce assets
        html.H2("Life Expectancy vs. GDP", className="title"),

        html.Div([
            html.Div([
                html.Label("Developing Status of the Country"),
                dcc.Dropdown(
                    id="status-dropdown", 
                    options=[{"label": data, "value": data} for data in df['Status'].unique()],
                    className="dropdown",
                    ),
                ]),
            html.Div([
                html.Label("Average schooling years greater than"),
                dcc.Dropdown(
                    id="schooling-dropdown",
                    options=[{"label": data, "value": data} for data in range(
                        int(df.Schooling.min()), int(df.Schooling.max()) + 1)
                    ],
                    className="dropdown",
                    ),
                ]),
            ],
            className="row",),

        html.Div(dcc.Graph(id="life-exp-vs-gdp"), className="chart"),

        dcc.Slider(
            id="year-slider",
            min=df['Year'].min(),
            max=df['Year'].max(),
            step=1,
            value=df['Year'].min(),
            marks={year: str(year) for year in range(df['Year'].min(), df['Year'].max() + 1)},
        ),        
    ],
    className="container",)

@app.callback(
    Output("life-exp-vs-gdp", "figure"),
    Input("status-dropdown", "value"),
    Input("schooling-dropdown", "value"),
    Input("year-slider", "value"),
)
def update_figure(country_status, min_schooling, selected_year):

    filtered_dataset = df[(df['Year'] == selected_year)]

    if min_schooling: 
        filtered_dataset = filtered_dataset[filtered_dataset['Schooling'] >= min_schooling]

    if country_status:
        filtered_dataset = filtered_dataset[filtered_dataset['Status'] == country_status]

    fig = px.scatter(
        filtered_dataset,
        x="GDP",
        y="Life expectancy",
        size="Population",
        color="continent",
        hover_name="Country",
        log_x=True,
        size_max=60,
    )

    #inline stylovani grafu (dynamicke)
    fig.update_layout(
        plot_bgcolor=colors["background"],
        paper_bgcolor=colors["background"],
        font_color=colors["text"],
    )

    return fig

if __name__ == "__main__":
    app.run_server(debug=True, port=9000)
