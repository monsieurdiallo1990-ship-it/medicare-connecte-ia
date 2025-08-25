import streamlit as st
import pandas as pd

st.set_page_config(page_title="Medicare Connect - Prototype", layout="wide")

st.title("Medicare Connect - Visualisation des demandes")
st.write("Prototype rapide pour explorer les données du fichier Medicare_Connect2025-08-15_17_23_42.csv")

# Chargement du fichier CSV
uploaded_file = st.file_uploader("Téléchargez votre fichier CSV", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success(f"{df.shape[0]} enregistrements chargés.")
    # Affichage des filtres
    with st.expander("Filtres avancés"):
        # Création de filtres dynamiques par colonnes principales
        col1, col2, col3 = st.columns(3)
        with col1:
            nom = st.text_input("Filtrer par nom")
        with col2:
            region = st.selectbox("Région", [""] + sorted(df["Régions de France"].dropna().unique().tolist()))
        with col3:
            langue = st.selectbox("Langue officielle", [""] + sorted(df["Langues officielles"].dropna().unique().tolist()))
        # Application des filtres
        filtered_df = df.copy()
        if nom:
            filtered_df = filtered_df[filtered_df["Last Name"].str.contains(nom, case=False, na=False)]
        if region:
            filtered_df = filtered_df[filtered_df["Régions de France"] == region]
        if langue:
            filtered_df = filtered_df[filtered_df["Langues officielles"] == langue]
    # Affichage du tableau filtré
    st.dataframe(filtered_df, use_container_width=True)
    st.download_button("Télécharger les résultats filtrés", data=filtered_df.to_csv(index=False), file_name="filtered_results.csv", mime="text/csv")
else:
    st.info("Veuillez ajouter un fichier CSV pour commencer.")