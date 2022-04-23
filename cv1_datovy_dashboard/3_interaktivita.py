from dash import Dash
from dash import dcc
from dash import html
from dash import Output         #callback do dekoratoru pro zobrazeni vystupni komponenty
from dash import Input          #callback do dekoratoru pro zmeny komponenty
import plotly.express as px
import pandas as pd

df = pd.read_csv(
    "https://raw.githubusercontent.com/ThuwarakeshM/geting-started-with-plottly-dash/main/life_expectancy.csv"
)

app = Dash()

app.layout = html.Div(
    [
        html.Div(
            [
                dcc.Dropdown(
                    id="status-dropdown",
                    options=[{"label": data, "value": data} for data in df['Status'].unique()],
                ),
            ]
        ),

        html.Div(
            [
                dcc.Dropdown(
                    id="schooling-dropdown",
                    options=[{"label": data, "value": data} for data in range(
                            int(df.Schooling.min()), int(df.Schooling.max()) + 1
                        )
                    ],
                ),
            ]
        ),

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
)

#dekorator, umoznujici vyuzivat paradigmat reaktivniho programovani (automaticka propagace zmen)
@app.callback(
    Output("life-exp-vs-gdp", "figure"),    #zavolanim se zmeni obsah grafu (figure) prvku s danym id
    Input("status-dropdown", "value"),      #prvnim z libovolneho poctu vstupnich argumentu, ktere
    Input("schooling-dropdown", "value"),   #   ovlivnuji vystupni prvek. Uvadi se id prvku a vlastnost,
    Input("year-slider", "value"),          #   ktera zmenu vyvolava (nejcasteji value)
)
#vyvolavajici vlastnost vstupnich prvku se stane argumentem dekorovane callback metody
def update_figure(country_status, min_schooling, selected_year):

    #z originalniho datasetu vrat pouze ty radky s pozadovanym rokem
    filtered_dataset = df[(df['Year'] == selected_year)]

    #pokud je zadana i minimalni prumerna delka studia, tak vyfiltruj
    if min_schooling: 
        filtered_dataset = filtered_dataset[filtered_dataset['Schooling'] >= min_schooling]

    #pokud je zadan i typ zeme (rozvijujici/rozvinuta), tak vyfiltruj
    if country_status:
        filtered_dataset = filtered_dataset[filtered_dataset['Status'] == country_status]

    #vytvor graf z vyfiltrovaneho datoveho ramce
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

    #vrat upraveny figure, vytvoreny z vyfiltrovanych dat, ktery se stane vystupnim callbackem
    return fig


if __name__ == "__main__":
    app.run_server(debug=True, port=9000)