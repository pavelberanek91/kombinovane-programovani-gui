#pokud neco posloucha na portu, tak:
#  sudo lsof -i :[cislo_portu]
#  kill -9 [pid]

#nacteni potrebnych modulu
from dash import Dash                   #trida, slouzici pro instantizaci dash aplikace
from dash import dcc                    #slouzi pro vytvareni komponent datoveho dashboardu
from dash import html                   #slouzi pro vytvoreni html prvku s navazanim komponent
import plotly.express as px             #slouzi pro vytvareni obsahu grafu (anglicky figure)
import pandas as pd                     #slouzi pro praci s tabulkovymi daty

#nacteni tabulkovych dat do datoveho ramce z csv souboru
df = pd.read_csv(
    #lze napsat umisteni na disku nebo i webove umisteni pomoci URL
    "https://raw.githubusercontent.com/ThuwarakeshM/geting-started-with-plottly-dash/main/life_expectancy.csv"
)

#vytvoreni grafu
fig = px.scatter(
    df,                     #data
    x="GDP",                #legenda na ose X
    y="Life expectancy",    #datova rada na ose Y
    size="Population",      #velikost kruznice na scatter-plotu
    size_max=60,            #omezeni maximalni velikosti kruznice
    color="continent",      #barva kruznice na scatter-plotu
    hover_name="Country",   #titulek pri najeti kurzorem na kruznici
    log_x=True,             #zapnuti logaritmicke skaly pro osu X
)

#instantizace Dash aplikace
app = Dash()

#prirazeni grafu do aplikace do html div elementu
app.layout = html.Div([dcc.Graph(id="life-exp-vs-gdp", figure=fig)])

#spusteni dash serveru na pozadovanem portu
if __name__ == "__main__":
    app.run_server(debug=True, port=9000)