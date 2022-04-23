# nacteni potrebnych modulu
import streamlit as st
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

# nastaveni vzhledu grafu podle seabornu
sns.set_theme()

#dekorator pro memoizaci funkce (cachovani vystupu funkce)
@st.cache
def load_data():
    df = pd.read_csv('voters_demo_sample.csv')
    return df

# nacteni dat do pandas datoveho ramce
df = load_data()

#spusteni vyhledani stredu klastru pomoci k-means metody
def run_kmeans(df, n_clusters=2):
    kmeans = KMeans(n_clusters, random_state=0).fit(df[["Age", "Income"]])
    fig, ax = plt.subplots(figsize=(16, 9))
    ax.grid(False)
    ax.set_facecolor("#FFF")
    ax.spines[["left", "bottom"]].set_visible(True)
    ax.spines[["left", "bottom"]].set_color("#4a4a4a")
    ax.tick_params(labelcolor="#4a4a4a")
    ax.yaxis.label.set(color="#4a4a4a", fontsize=20)
    ax.xaxis.label.set(color="#4a4a4a", fontsize=20)

    # vytvor seaborn grafy typu scatterplot
    ax = sns.scatterplot(
        ax=ax,
        x=df.Age,
        y=df.Income,
        hue=kmeans.labels_,
        palette=sns.color_palette("colorblind", n_colors=n_clusters),
        legend=None,
    )

    # anotuj stredy klastru
    for ix, [age, income] in enumerate(kmeans.cluster_centers_):
        ax.scatter(age, income, s=200, c="#a8323e")
        ax.annotate(
            f"Cluster #{ix+1}",
            (age, income),
            fontsize=25,
            color="#a8323e",
            xytext=(age + 5, income + 3),
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="#a8323e", lw=2),
            ha="center",
            va="center",
        )

    return fig

# vytvoreni bocni listy s ovladacimi prvky
sidebar = st.sidebar

# vytvoreni tlacitka do bocni listy pro zobrazeni raw dat
df_display = sidebar.checkbox("Display Raw Data", value=True)

# vytvoreni posunovace poctu zvolenych klasteru
n_clusters = sidebar.slider(
    "Select Number of Clusters",
    min_value=2,
    max_value=10,
)

# text do bocni listy
sidebar.write(
    """
    Hello world from streamlit.
    """
)

# nazev streamlit aplikace
st.title("K-Means Clustering")

# vytvor seaborn k-means graf
st.write(run_kmeans(df, n_clusters=n_clusters))

# zobraz streamlit graf
if df_display:
    st.write(df)