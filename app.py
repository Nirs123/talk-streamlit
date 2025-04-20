import streamlit as st
import pandas as pd
import requests

# Étape 1
st.set_page_config(
    page_title="Pokemon dataset explorer",
    page_icon=":dragon:",
    layout="wide"
)
st.title("Pokemon dataset explorer")
st.text("Explorateur de données Pokemon")

# Étape 5
dataframe_col, graph_col, image_col = st.columns(3)

with dataframe_col:
    # Étape 2
    dataset = pd.read_csv("pokemon_dataset.csv")
    # Étape 3
    types = st.multiselect("Types de pokémon", options=dataset["Type 1"].unique())
    # Étape 4
    min_power = st.slider(
        "Puissance d'attaque minimum",
        min_value=min(dataset["Att"]),
        max_value=max(dataset["Att"]),
        value=min(dataset["Att"])
    )
    # Étape 2
    st.dataframe(
        dataset[dataset["Type 1"].isin(types) & (dataset["Att"] >= min_power)]
    )

with graph_col:
    # Étape 7
    stat = st.radio("Statistique de l'histogramme", options=["HP", "Att", "Def", "Spe"])
    st.text(f"Répartition {stat}")
    # Étape 6
    st.bar_chart(
        data=dataset[dataset["Type 1"].isin(types) & (dataset["Att"] >= min_power)][stat].value_counts()
    )

with image_col:
    # Étape 8
    st.text("Sélectionnez un pokémon")
    pokemon = st.selectbox("Pokémon", options=dataset["Name"])
    
    url = f"https://img.pokemondb.net/artwork/large/{pokemon.lower()}.jpg"
    
    if requests.head(url).status_code == 200:
        st.image(url)
    else:
        st.error("Cette image n'est pas disponible")
