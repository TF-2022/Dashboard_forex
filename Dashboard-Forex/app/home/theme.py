import streamlit as st


def Theme_fond():

    # Affichage d'un texte coloré avec la couleur sélectionnée
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: linear-gradient(to bottom,#000000, #182848);
            border-radius: 20px;
            padding: 2rem;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

Theme_fond()