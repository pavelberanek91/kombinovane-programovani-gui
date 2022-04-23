from dash import Dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd

df = pd.read_csv(
    "https://raw.githubusercontent.com/ThuwarakeshM/geting-started-with-plottly-dash/main/life_expectancy.csv"
)

fig = px.scatter(
    df,
    x="GDP",
    y="Life expectancy",
    size="Population",
    size_max=60,
    color="continent",
    hover_name="Country",
    log_x=True,
)

app = Dash()

#tvorba rozvrzeni datoveho dashboardu
app.layout = html.Div(
    [
        #vytvoreni komponenty ve forme elementu div
        html.Div(
            [
                #seznam pro vyber filtru na rozvijejici a rozvinute zeme
                dcc.Dropdown(
                    
                    #id div elementu
                    id="status-dropdown",
                    
                    #prvky seznamu ziskane z datoveho ramce (diky unique zapocitany jen jednou)
                    options=[{"label": data, "value": data} for data in df['Status'].unique()],
                ),
            ]
        ),

        # seznam pro vuber filtru na dobu povinne skolni dochazky
        html.Div(
            [
                dcc.Dropdown(
                    id="schooling-dropdown",
                    
                    #range ma maximum exkluzivni, proto musime uvadet + 1
                    options=[{"label": data, "value": data} for data in range(
                            int(df.Schooling.min()), int(df.Schooling.max()) + 1
                        )
                    ],
                ),
            ]
        ),

        #misto pro ulozeni grafu (placeholder), posunovac ma byt az pod grafem
        html.Div(dcc.Graph(id="life-exp-vs-gdp"), className="chart"),

        #posunovac pro vyber roku v grafu
        dcc.Slider(
            id="year-slider",       #id html elementu pro posunovac (volitelne)
            min=df['Year'].min(),   #nastav minimalni hodnotu posunovace
            max=df['Year'].max(),   #nastav maximalni hodnotu posunovace
            step=1,                 #krok posunovace
            value=df['Year'].min(), #pocatecni hodnota pri nacteni komponenty
            #popisek dat na posunovaci ve forme slovniku {data:popisek}
            marks={year: str(year) for year in range(df['Year'].min(), df['Year'].max() + 1)},
        ),        
    ],
)

if __name__ == "__main__":
    app.run_server(debug=True, port=9000)