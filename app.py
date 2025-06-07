import streamlit as st
import pandas as pd
import requests

st.set_page_config(
    page_title="Pokemon dataset explorer",
    page_icon=":dragon:",
    layout="wide"
)
st.title("Pokemon dataset explorer")
st.text("Explorateur de données Pokemon")

dataframe_col, graph_col, image_col = st.columns(3)

with dataframe_col:
    dataset = pd.read_csv("pokemon_dataset.csv")
    types = st.multiselect("Types de pokémon", options=dataset["Type"].unique())
    min_power = st.slider(
        "Puissance d'attaque minimum",
        min_value=min(dataset["Att"]),
        max_value=max(dataset["Att"]),
        value=min(dataset["Att"])
    )
    st.dataframe(
        dataset[dataset["Type"].isin(types) & (dataset["Att"] >= min_power)]
    )

with graph_col:
    stat = st.radio("Statistique de l'histogramme", options=["HP", "Att", "Def", "Spe"])
    st.text(f"Répartition {stat}")
    st.bar_chart(
        data=dataset[dataset["Type"].isin(types) & (dataset["Att"] >= min_power)][stat].value_counts()
    )

with image_col:
    st.text("Sélectionnez un pokémon")
    pokemon = st.selectbox("Pokémon", options=dataset["Name"])
    
    url = f"https://img.pokemondb.net/artwork/large/{pokemon.lower()}.jpg"
    
    if requests.head(url).status_code == 200:
        st.image(url)
    else:
        st.error("Cette image n'est pas disponible")
